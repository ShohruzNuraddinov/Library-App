from rest_framework import generics

from apps.library.models import Book
from apps.library.api_endpoints.Book.serializers import BookSerializer


class BookAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a book.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    http_method_names = ["get", "patch", "delete"]


__all__ = ["BookAPIView"]
