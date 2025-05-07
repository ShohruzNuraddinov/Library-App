from rest_framework import generics


from apps.library.models import Genre


class GenderDeleteAPIView(generics.DestroyAPIView):
    """
    API view for deleting a genre.
    """
    queryset = Genre.objects.all()


__all__ = ["GenderDeleteAPIView"]
