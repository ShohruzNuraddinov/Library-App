from rest_framework import generics

from apps.users.api_endpoints.Profile.serializers import ProfileSerializer


class ProfileAPIView(generics.RetrieveAPIView):
    """
    API view for user profile.
    """
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


__all__ = ["ProfileAPIView"]
