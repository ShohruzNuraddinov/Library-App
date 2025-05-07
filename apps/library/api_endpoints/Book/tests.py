from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from apps.library.models import Book, Author, Genre


class BookAPIViewTestCase(APITestCase):
    def setUp(self):
        # Create user and authenticate
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='securepassword123'
        )
        self.client.force_authenticate(user=self.user)

        # Create Genre, Author, Book
        self.genre = Genre.objects.create(name="Fiction")
        self.author = Author.objects.create(
            first_name="George",
            last_name="Orwell",
            birth_date="1903-06-25",
            death_date="1950-01-21"
        )
        self.book = Book.objects.create(
            title="1984",
            description="Dystopian novel",
            genre=self.genre,
            length=328,
            published_date="1949-06-08",
            created_date="1949-06-08",
            copies_sold=30000000,
            price=19.99,
            discount=0.0,
            cover="covers/1984.jpg",
            author=self.author
        )
        self.url = reverse("library:book-detail", kwargs={"pk": self.book.pk})

    def test_get_book_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")
        self.assertEqual(response.data["author"]["first_name"], "George")
        self.assertEqual(response.data["genre"], "Fiction")

    def test_get_book_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_book_author(self):
        new_author = Author.objects.create(
            first_name="Aldous",
            last_name="Huxley",
            birth_date="1894-07-26",
            death_date="1963-11-22"
        )
        data = {"author_id": new_author.pk}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.author.first_name, "Aldous")

    def test_delete_book(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
