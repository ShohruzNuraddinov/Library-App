from django.urls import path

from apps.library.api_endpoints import *

app_name = "library"

urlpatterns = [
    path("books/<int:pk>/", BookAPIView.as_view(), name="book-detail"),
    path("books/<int:pk>/rate/", RateAPIView.as_view(), name="rate-book"),
    path("books/create/", BookCreateAPIView.as_view(), name="create-book"),
    path("genre/<int:pk>/", GenderDeleteAPIView.as_view(), name="delete-genre"),

    path("authors/", AuthorListCreateAPIView.as_view(), name="authors"),
    path("authors/<int:pk>/", AuthorAPIView.as_view(), name="author")
]
