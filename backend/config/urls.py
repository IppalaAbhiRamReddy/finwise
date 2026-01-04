from django.urls import path, include
from .health import health_check



urlpatterns = [
    path("api/health/", health_check),
    path("api/", include("core.urls")),
    path("api/", include("users.urls")),
    path("api/auth/", include("authn.urls")),
]
