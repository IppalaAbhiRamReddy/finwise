from rest_framework.throttling import UserRateThrottle

class DashboardThrottle(UserRateThrottle):
    rate = "60/min"


class AlertsThrottle(UserRateThrottle):
    rate = "30/min"
