from rest_framework import generics

from apps.library.api_endpoints.AuthorListCreate.serializers import AuthorSerializer
from apps.library.models import Author


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all().prefetch_related("books")


__all__ = ["AuthorListCreateAPIView"]
