"""
User profile model.

Purpose:
- Store user-specific preferences and metadata
- Financial logic is NOT handled here
"""

from django.conf import settings
from django.db import models


class Profile(models.Model):
    """
    Extends the default User model with financial preferences.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    # Monthly income declared by the user (used only for insights, not enforcement)
    monthly_income = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Currency preference (ISO code like INR, USD)
    currency = models.CharField(
        max_length=10,
        default="INR"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile({self.user.username})"
