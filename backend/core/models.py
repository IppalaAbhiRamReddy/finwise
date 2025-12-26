"""
Core financial data models.

Includes:
- Transaction
- Budget
- Goal
"""

from django.conf import settings
from django.db import models


class Transaction(models.Model):
    """
    Represents a single financial event.
    Immutable by default once created.
    """

    INCOME = "income"
    EXPENSE = "expense"

    TRANSACTION_TYPES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    # Whether this transaction is income or expense
    type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    # User-defined category (no auto categorization)
    category = models.CharField(
        max_length=100
    )

    # Amount involved in the transaction
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Date when transaction occurred (can differ from creation time)
    date = models.DateField()

    # Optional user note
    note = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"

#BUDGETS 
class Budget(models.Model):
    """
    Represents a spending limit for a specific category and time range.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="budgets"
    )

    # Category this budget applies to
    category = models.CharField(
        max_length=100
    )

    # Maximum allowed spending
    limit_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Budget({self.category} - {self.limit_amount})"
    
#GOALS
class Goal(models.Model):
    """
    Represents a financial saving goal.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="goals"
    )

    # User-defined goal name
    name = models.CharField(
        max_length=100
    )

    target_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Amount saved so far (updated explicitly, not derived yet)
    saved_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Goal({self.name})"
