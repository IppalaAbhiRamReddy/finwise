"""
Authentication URL routes.
"""
from django.urls import path
from .views import LoginView, ProtectedTestView

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("protected/", ProtectedTestView.as_view()),
]
