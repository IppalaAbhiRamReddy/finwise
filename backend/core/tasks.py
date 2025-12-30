"""
Celery tasks for alerts and ML insights.
"""

from celery import shared_task
from django.contrib.auth.models import User

from core.services.ml_adapter import fetch_ml_insights
from core.services.alerts import generate_rule_based_alerts


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 3})
def run_alerts_for_user(self, user_id):
    """
    Background task to compute alerts for a user.
    Safe to retry and fail silently.
    """
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return []

    rule_alerts = generate_rule_based_alerts(user)
    ml_alerts = fetch_ml_insights(user.id)

    return rule_alerts + ml_alerts
