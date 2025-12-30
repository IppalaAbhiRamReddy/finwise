"""
API views for core financial entities.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Transaction, Budget, Goal
from .serializers import (
    TransactionSerializer,
    BudgetSerializer,
    GoalSerializer,
)


class TransactionListCreateView(APIView):
    """
    Create and list transactions for the authenticated user.
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
        return Response(serializer.data, status=201)

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

class GoalListCreateView(APIView):
    """
    Create and list goals for the authenticated user.
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


"""
Dashboard API view.

Purpose:
- Aggregate financial data for the dashboard
- Serve a single, optimized response
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.services.dashboard import (
    get_current_month,
    get_monthly_transactions,
    calculate_totals,
    category_breakdown,
    budget_usage,
    goal_progress,
)


from core.services.insights import generate_insights
class DashboardSummaryView(APIView):
    """
    Returns summarized dashboard data for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
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
            "insights": generate_insights(user, transactions)

        }

        return Response(response)

"""
Alerts API view.

Purpose:
- Aggregate rule-based alerts and ML insights
- Return a unified alerts list
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.services.alerts import generate_rule_based_alerts
from core.services.ml_adapter import fetch_ml_insights


class AlertsView(APIView):
    """
    Returns alerts for the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        rule_alerts = generate_rule_based_alerts(user)
        ml_alerts = fetch_ml_insights(user.id)

        alerts = rule_alerts + ml_alerts

        return Response({
            "alerts": alerts
        })
