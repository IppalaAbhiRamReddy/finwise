"""
Dashboard aggregation services.

Purpose:
- Compute financial summaries for dashboard
- NO database writes
- NO ML logic
"""

from collections import defaultdict
from django.db.models import Sum
from datetime import date

from core.models import Transaction, Budget, Goal


def get_current_month():
    """
    Returns the current year-month string.
    """
    today = date.today()
    return today.strftime("%Y-%m")


def get_monthly_transactions(user):
    """
    Fetch all transactions for the current month.
    """
    today = date.today()
    return Transaction.objects.filter(
        user=user,
        date__year=today.year,
        date__month=today.month
    )


def calculate_totals(transactions):
    """
    Calculate income, expense, and savings.
    """
    income = transactions.filter(type="income").aggregate(
        total=Sum("amount")
    )["total"] or 0

    expense = transactions.filter(type="expense").aggregate(
        total=Sum("amount")
    )["total"] or 0

    return {
        "income": income,
        "expense": expense,
        "savings": income - expense
    }


def category_breakdown(transactions):
    """
    Group expenses by category.
    """
    category_map = defaultdict(float)

    for tx in transactions.filter(type="expense"):
        category_map[tx.category] += float(tx.amount)

    return [
        {"category": k, "expense": v}
        for k, v in category_map.items()
    ]


def budget_usage(user, transactions):
    """
    Compare budgets against actual spending.
    """
    budgets = Budget.objects.filter(user=user)
    expenses = defaultdict(float)

    for tx in transactions.filter(type="expense"):
        expenses[tx.category] += float(tx.amount)

    results = []
    for budget in budgets:
        spent = expenses.get(budget.category, 0)
        status = "ok" if spent <= float(budget.limit_amount) else "exceeded"

        results.append({
            "category": budget.category,
            "limit": float(budget.limit_amount),
            "spent": spent,
            "status": status
        })

    return results


def goal_progress(user):
    """
    Calculate progress percentage for goals.
    """
    goals = Goal.objects.filter(user=user)

    results = []
    for goal in goals:
        progress = (
            (goal.saved_amount / goal.target_amount) * 100
            if goal.target_amount > 0 else 0
        )

        results.append({
            "name": goal.name,
            "target": float(goal.target_amount),
            "saved": float(goal.saved_amount),
            "progress_percent": round(progress, 2)
        })

    return results
