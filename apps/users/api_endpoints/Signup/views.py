from rest_framework import generics, permissions

from apps.users.api_endpoints.Signup.serializers import SignupSerializer


class SignupAPIView(generics.CreateAPIView):
    """
    API view for user signup.
    """
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
    
__all__ = ["SignupAPIView"]
