from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from apps.library.models import Author, Book, Genre


class BookCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@test.com",
            password="securepass123"
        )
        self.client.force_authenticate(user=self.user)

        self.author = Author.objects.create(
            first_name="Isaac",
            last_name="Asimov",
            birth_date="1920-01-02",
            death_date="1992-04-06"
        )
        self.genre = Genre.objects.create(name="Science Fiction")

        self.url = reverse("library:create-book")

    def test_create_book_success(self):
        data = {
            "author_id": self.author.id,
            "title": "Foundation",
            "description": "A science fiction novel about the fall of the Galactic Empire.",
            "genre": self.genre.id,
            "length": 255,
            "published_date": "1951-01-01",
            "created_date": "1951-01-01",
            "copies_sold": 5000000,
            "price": "14.99",
            "discount": 5.0
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.first()
        self.assertEqual(book.title, "Foundation")
        self.assertEqual(book.author, self.author)

    def test_create_book_invalid_author(self):
        data = {
            "author_id": 9999,
            "title": "Fake Book",
            "description": "Doesn't matter.",
            "genre": self.genre.id,
            "length": 100,
            "published_date": "2000-01-01",
            "created_date": "2000-01-01",
            "copies_sold": 0,
            "price": 10.0,
            "discount": 0.0,
            "cover": ""
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("author_id", response.data)

    def test_create_book_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            "author_id": self.author.id,
            "title": "I, Robot",
            "description": "Classic robot stories.",
            "genre": self.genre.name,
            "length": 300,
            "published_date": "1950-12-02",
            "created_date": "1950-12-02",
            "copies_sold": 1000000,
            "price": 12.99,
            "discount": 0.0,
            "cover": "covers/irobot.jpg"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
