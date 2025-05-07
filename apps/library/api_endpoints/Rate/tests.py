from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from apps.library.models import Book, Rating, Genre, Author


class RateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@test.com",
            password="securepassword123"
        )
        self.client.force_authenticate(user=self.user)
        self.genre = Genre.objects.create(name="Fiction")

        self.author = Author.objects.create(
            first_name="Isaac",
            last_name="Asimov",
            birth_date="1920-01-02",
            death_date="1992-04-06"
        )

        self.book = Book.objects.create(
            title="Test Book",
            description="A test book",
            genre=self.genre,
            author=self.author,
            length=100,
            published_date="2023-01-01",
            price=9.99,
        )

        self.url = reverse("library:rate-book", kwargs={"pk": self.book.pk})

    def test_rate_book_authenticated(self):
        data = {"rate": 5}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 1)
        rating = Rating.objects.first()
        self.assertEqual(rating.rate, 5)
        self.assertEqual(rating.user, self.user)
        self.assertEqual(rating.book, self.book)

    def test_rate_book_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {"rate": 4}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_rate_non_existent_book(self):
        invalid_url = reverse("library:rate-book", kwargs={"pk": 9999})
        data = {"rate": 4}
        response = self.client.post(invalid_url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
