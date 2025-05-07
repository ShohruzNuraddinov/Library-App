from rest_framework import generics

from apps.library.models import Book
from apps.library.api_endpoints.BookCreate.serializers import BookCreateSerializer


class BookCreateAPIView(generics.CreateAPIView):
    """
    API view for creating a book.
    """
    serializer_class = BookCreateSerializer
    queryset = Book.objects.all()


__all__ = ["BookCreateAPIView"]
