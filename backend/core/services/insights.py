"""
Rule-based insights engine.

Purpose:
- Generate explainable insights from financial data
- Acts as fallback when ML is unavailable
"""

from django.db.models import Sum
from datetime import date, timedelta

from core.models import Transaction


def month_expense(user, year, month):
    """
    Calculate total expenses for a given month.
    """
    return (
        Transaction.objects.filter(
            user=user,
            type="expense",
            date__year=year,
            date__month=month
        ).aggregate(total=Sum("amount"))["total"]
        or 0
    )


def spending_trend_insight(user):
    """
    Compare current month expenses with previous month.
    """
    today = date.today()
    current = month_expense(user, today.year, today.month)

    prev_month = today.replace(day=1) - timedelta(days=1)
    previous = month_expense(user, prev_month.year, prev_month.month)

    if previous == 0:
        return None

    diff_percent = ((current - previous) / previous) * 100

    if diff_percent > 10:
        return f"Your expenses increased by {round(diff_percent, 1)}% compared to last month"
    elif diff_percent < -10:
        return f"Good job! Your expenses decreased by {abs(round(diff_percent, 1))}% compared to last month"

    return None


def top_category_insight(transactions):
    """
    Identify highest spending category.
    """
    category_totals = {}

    for tx in transactions.filter(type="expense"):
        category_totals[tx.category] = category_totals.get(tx.category, 0) + float(tx.amount)

    if not category_totals:
        return None

    top_category = max(category_totals, key=category_totals.get)
    return f"{top_category} is your highest spending category"


def generate_insights(user, transactions):
    """
    Generate a list of insights.
    """
    insights = []

    trend = spending_trend_insight(user)
    if trend:
        insights.append(trend)

    category = top_category_insight(transactions)
    if category:
        insights.append(category)

    return insights
