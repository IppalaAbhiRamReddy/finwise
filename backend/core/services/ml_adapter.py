"""
External ML adapter.

Purpose:
- Safely consume ML insights
- Fail silently and return empty insights on error
"""

import requests


ML_SERVICE_URL = "https://example-ml-service/api/insights"
TIMEOUT_SECONDS = 2


def fetch_ml_insights(user_id):
    """
    Fetch ML-generated insights for a user.

    Returns:
    - List of insight messages
    - Empty list on failure
    """
    try:
        response = requests.post(
            ML_SERVICE_URL,
            json={"user_id": user_id},
            timeout=TIMEOUT_SECONDS
        )

        if response.status_code != 200:
            return []

        data = response.json()
        return [
            item.get("message")
            for item in data.get("insights", [])
            if "message" in item
        ]

    except Exception:
        # Silent failure: ML must never break the system
        return []
