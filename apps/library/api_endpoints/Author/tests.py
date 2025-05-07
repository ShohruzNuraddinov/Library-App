from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.library.models import Author, Book, Genre  # Assuming a Genre model exists

User = get_user_model()


class AuthorAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com', password='securepass')
        self.client.force_authenticate(user=self.user)

        self.genre = Genre.objects.create(name='Fiction')
        self.author = Author.objects.create(
            first_name='Leo',
            last_name='Tolstoy',
            birth_date='1828-09-09',
            death_date='1910-11-20'
        )
        self.book = Book.objects.create(
            title='War and Peace',
            description='A historical novel',
            genre=self.genre,
            length=1225,
            published_date='1869-01-01',
            created_date='1869-01-01',
            copies_sold=1000000,
            price=39.99,
            discount=10.0,
            cover='covers/war_and_peace.jpg',
            author=self.author
        )
        self.url = reverse('library:author', kwargs={'pk': self.author.pk})

    def test_get_author_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Leo')
        self.assertEqual(response.data['books'][0]['title'], 'War and Peace')

    def test_get_author_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_author(self):
        data = {'first_name': 'Lev'}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.first_name, 'Lev')

    def test_delete_author(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Author.objects.filter(pk=self.author.pk).exists())
