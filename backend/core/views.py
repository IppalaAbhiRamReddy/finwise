"""
API views for core financial entities, dashboard, and alerts.

This module contains:
- CRUD APIs for Transactions, Budgets, and Goals
- Read-only Dashboard Summary API
- Alerts aggregation API (rule-based + ML)

Performance Enhancements (Phase 4.1):
- Redis caching for dashboard and alerts
- Safe cache invalidation on transaction creation
- Graceful fallback if Redis is unavailable
"""

from datetime import date

from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import Profile
from core.throttles import DashboardThrottle,AlertsThrottle

from .models import Transaction, Budget, Goal
from .serializers import (
    TransactionSerializer,
    BudgetSerializer,
    GoalSerializer,
)

from core.services.dashboard import (
    get_current_month,
    get_monthly_transactions,
    calculate_totals,
    category_breakdown,
    budget_usage,
    goal_progress,
)

from core.services.insights import generate_insights
from core.services.alerts import generate_rule_based_alerts
from core.services.ml_adapter import fetch_ml_insights


# -------------------------------------------------------------------
# TRANSACTIONS API
# -------------------------------------------------------------------

class TransactionListCreateView(APIView):
    """
    Create and list transactions for the authenticated user.

    Performance notes:
    - On transaction creation, dashboard and alerts caches are invalidated
    - This ensures users always see fresh insights after adding data
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        # ------------------------------
        # Cache invalidation (CRITICAL)
        # ------------------------------
        month_key = date.today().strftime("%Y-%m")
        cache.delete(f"dashboard:{request.user.id}:{month_key}")
        cache.delete(f"alerts:{request.user.id}")

        return Response(serializer.data, status=201)


# -------------------------------------------------------------------
# BUDGETS API
# -------------------------------------------------------------------

class BudgetListCreateView(APIView):
    """
    Create and list budgets for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        budgets = Budget.objects.filter(user=request.user)
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=201)


# -------------------------------------------------------------------
# GOALS API
# -------------------------------------------------------------------

class GoalListCreateView(APIView):
    """
    Create and list financial goals for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        goals = Goal.objects.filter(user=request.user)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GoalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=201)


# -------------------------------------------------------------------
# DASHBOARD SUMMARY API (CACHED)
# -------------------------------------------------------------------

class DashboardSummaryView(APIView):
    """
    Returns summarized dashboard data for the authenticated user.

    Performance:
    - Cached per user per month
    - Cache TTL: 60 seconds
    - Gracefully falls back to live computation if cache is unavailable
    """
    permission_classes = [IsAuthenticated]
    throttle_classes = [DashboardThrottle]

    def get(self, request):
        user = request.user
        month_key = date.today().strftime("%Y-%m")
        cache_key = f"dashboard:{user.id}:{month_key}"

        # Attempt cache read
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response)
        
        profile, _ = Profile.objects.get_or_create(user=user)

        # Cache miss → compute dashboard
        transactions = get_monthly_transactions(user)

        response = {
            "period": {
                "month": get_current_month(),
                "currency": getattr(user.profile, "currency", "INR")
            },
            "totals": calculate_totals(transactions),
            "categories": category_breakdown(transactions),
            "budgets": budget_usage(user, transactions),
            "goals": goal_progress(user),
            "insights": generate_insights(user, transactions),
        }

        # Store in cache (short TTL)
        cache.set(cache_key, response, timeout=60)

        return Response(response)


# -------------------------------------------------------------------
# ALERTS API (CACHED)
# -------------------------------------------------------------------

class AlertsView(APIView):
    """
    Returns financial alerts for the authenticated user.

    Alerts include:
    - Rule-based alerts (always available)
    - Optional ML-generated insights (safe fallback)

    Performance:
    - Cached per user
    - Cache TTL: 30 seconds
    """
    permission_classes = [IsAuthenticated]
    throttle_classes = [AlertsThrottle]

    def get(self, request):
        user = request.user
        cache_key = f"alerts:{user.id}"

        # Attempt cache read
        cached_alerts = cache.get(cache_key)
        if cached_alerts:
            return Response({"alerts": cached_alerts})

        # Cache miss → compute alerts
        rule_alerts = generate_rule_based_alerts(user)
        ml_alerts = fetch_ml_insights(user.id)

        alerts = rule_alerts + ml_alerts

        # Store in cache
        cache.set(cache_key, alerts, timeout=30)

        return Response({"alerts": alerts})
