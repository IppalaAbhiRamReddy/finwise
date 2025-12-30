"""
Rule-based alerts engine.

Purpose:
- Detect risky financial behavior
- Generate human-readable alerts
"""

from datetime import date
from django.db.models import Sum

from core.models import Transaction, Budget


def budget_overuse_alerts(user):
    """
    Detect budget overuse for the current month.
    """
    alerts = []
    today = date.today()

    budgets = Budget.objects.filter(user=user)
    for budget in budgets:
        spent = (
            Transaction.objects.filter(
                user=user,
                type="expense",
                category=budget.category,
                date__year=today.year,
                date__month=today.month
            ).aggregate(total=Sum("amount"))["total"]
            or 0
        )

        if spent > budget.limit_amount:
            alerts.append(
                f"You have exceeded your {budget.category} budget for this month."
            )

    return alerts


def low_savings_alert(user):
    """
    Alert if savings rate is low.
    """
    today = date.today()

    income = (
        Transaction.objects.filter(
            user=user,
            type="income",
            date__year=today.year,
            date__month=today.month
        ).aggregate(total=Sum("amount"))["total"]
        or 0
    )

    expense = (
        Transaction.objects.filter(
            user=user,
            type="expense",
            date__year=today.year,
            date__month=today.month
        ).aggregate(total=Sum("amount"))["total"]
        or 0
    )

    if income == 0:
        return None

    savings_rate = (income - expense) / income

    if savings_rate < 0.10:
        return "Your savings rate is low this month. Consider reducing discretionary spending."

    return None


def unusual_spending_alert(user):
    """
    Detect unusually high spending compared to last 3 months average.
    """
    today = date.today()

    current = (
        Transaction.objects.filter(
            user=user,
            type="expense",
            date__year=today.year,
            date__month=today.month
        ).aggregate(total=Sum("amount"))["total"]
        or 0
    )

    past_totals = []
    for i in range(1, 4):
        prev_month = today.replace(day=1)
        prev_month = prev_month.replace(month=prev_month.month - i if prev_month.month > i else 12)

        total = (
            Transaction.objects.filter(
                user=user,
                type="expense",
                date__year=prev_month.year,
                date__month=prev_month.month
            ).aggregate(total=Sum("amount"))["total"]
            or 0
        )
        if total:
            past_totals.append(total)

    if not past_totals:
        return None

    average = sum(past_totals) / len(past_totals)

    if current > average * 1.3:
        return "Your spending this month is unusually high compared to previous months."

    return None


def generate_rule_based_alerts(user):
    """
    Aggregate all rule-based alerts.
    """
    alerts = []

    alerts.extend(budget_overuse_alerts(user))

    low_savings = low_savings_alert(user)
    if low_savings:
        alerts.append(low_savings)

    unusual = unusual_spending_alert(user)
    if unusual:
        alerts.append(unusual)

    return alerts
