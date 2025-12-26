from django.urls import path, include

urlpatterns = [
    path("api/", include("core.urls")),
    path("api/", include("users.urls")),
    path("api/auth/", include("authn.urls")),
]
