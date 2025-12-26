"""
Serializers for user-related data.

Purpose:
- Validate incoming profile data
- Control what fields are writable
"""

from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile.
    """

    class Meta:
        model = Profile
        fields = ["monthly_income", "currency"]

    def validate_monthly_income(self, value):
        """
        Monthly income must be non-negative.
        """
        if value < 0:
            raise serializers.ValidationError("Monthly income cannot be negative.")
        return value

