from rest_framework import generics

from apps.library.models import Author
from apps.library.api_endpoints.Author.serializers import AuthorSerializer


class AuthorAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    http_method_names = ["get", "patch", "delete"]


__all__ = ["AuthorAPIView"]
