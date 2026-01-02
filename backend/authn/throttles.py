"""
Custom throttles for authentication abuse protection.
"""

from rest_framework.throttling import SimpleRateThrottle


class LoginThrottle(SimpleRateThrottle):
    scope = "login"

    def get_cache_key(self, request, view):
        # Throttle by IP address
        return self.get_ident(request)


class RefreshThrottle(SimpleRateThrottle):
    scope = "refresh"

    def get_cache_key(self, request, view):
        return self.get_ident(request)
