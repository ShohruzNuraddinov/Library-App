from rest_framework import generics, permissions

from apps.users.api_endpoints.Login.serializers import LoginSerializer


class LoginAPIView(generics.CreateAPIView):
    """
    API view for user login.
    """
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]