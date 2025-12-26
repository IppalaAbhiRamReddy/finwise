"""
Serializers for core financial models.
"""

from rest_framework import serializers
from .models import Transaction, Budget, Goal


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for validating transaction input.
    """

    class Meta:
        model = Transaction
        fields = [
            "type",
            "category",
            "amount",
            "date",
            "note"
        ]

    def validate_amount(self, value):
        """
        Transaction amount must be positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

class BudgetSerializer(serializers.ModelSerializer):
    """
    Serializer for budget validation.
    """

    class Meta:
        model = Budget
        fields = [
            "category",
            "limit_amount",
            "start_date",
            "end_date"
        ]

    def validate_limit_amount(self, value):
        """
        Budget limit must be positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Budget limit must be greater than zero.")
        return value

    def validate(self, data):
        """
        Ensure start_date is before end_date.
        """
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError(
                "Budget start date must be before end date."
            )
        return data

class GoalSerializer(serializers.ModelSerializer):
    """
    Serializer for goal validation.
    """

    class Meta:
        model = Goal
        fields = [
            "name",
            "target_amount",
            "saved_amount",
            "deadline"
        ]

    def validate_target_amount(self, value):
        """
        Goal target must be positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Target amount must be greater than zero.")
        return value

    def validate_saved_amount(self, value):
        """
        Saved amount cannot be negative.
        """
        if value < 0:
            raise serializers.ValidationError("Saved amount cannot be negative.")
        return value

