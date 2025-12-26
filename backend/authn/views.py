"""
Authentication skeleton views.

Purpose:
- Verify request/response wiring
- Provide placeholder endpoints for later expansion
- NO real authentication logic in this phase
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    """
    Temporary login endpoint.
    Returns a dummy token to validate frontend-backend connectivity.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        return Response({
            "access": "dummy-access-token",
            "refresh": "dummy-refresh-token"
        })


class ProtectedTestView(APIView):
    """
    Endpoint to confirm protected route wiring.
    Will be secured properly in later phases.
    """
    def get(self, request):
        return Response({"message": "Authenticated access OK"})
