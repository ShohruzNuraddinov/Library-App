from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.library.models import Rating, Book
from apps.library.api_endpoints.Rate.serializers import RateSerializer


class RateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RateSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, book=book)


__all__ = ["RateAPIView"]
