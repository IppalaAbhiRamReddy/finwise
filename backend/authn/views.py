"""
Authentication views.

Implements:
- Login with JWT access token
- Refresh token via HttpOnly cookie
- Secure logout
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from .throttles import LoginThrottle
from django.contrib.auth.models import User


class LoginView(APIView):
    """
    Authenticates user and issues JWT tokens.
    Refresh token is stored as HttpOnly cookie.
    """
    permission_classes = [AllowAny]
    throttle_classes = [LoginThrottle]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        response = Response({
            "access": str(refresh.access_token)
        })

        # Store refresh token securely in cookie
        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            samesite="Lax",
            secure=False,  # True in production
            max_age=7 * 24 * 60 * 60,
        )

        return response

class RefreshView(APIView):

    permission_classes = [AllowAny]
    throttle_classes = [RefreshThrottle]

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response(
                {"detail": "NO REFRESH COOKIE"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            # Parse old refresh token
            old_refresh = RefreshToken(refresh_token)

            # Extract user_id
            user_id = old_refresh["user_id"]

            # Fetch user safely
            user = User.objects.get(id=user_id)

            # Issue new refresh + access tokens
            new_refresh = RefreshToken.for_user(user)
            new_access = str(new_refresh.access_token)

            response = Response(
                {"access": new_access},
                status=status.HTTP_200_OK
            )

            # Rotate refresh cookie
            response.set_cookie(
                key="refresh_token",
                value=str(new_refresh),
                httponly=True,
                samesite="Lax",
                secure=False,  # True in production
                max_age=7 * 24 * 60 * 60,
            )

            # Blacklist old refresh token (AFTER issuing new)
            old_refresh.blacklist()

            return response

        except Exception as e:
            print("REFRESH ERROR:", e)
            return Response(
                {"detail": str(e)},
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):
    """
    Clears refresh token cookie.
    Logout should not require authentication.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        response = Response({"detail": "Logged out"})
        response.delete_cookie("refresh_token")
        return response
