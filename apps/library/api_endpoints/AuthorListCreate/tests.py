from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from apps.library.models import Author


class AuthorListCreateAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='strongpassword123'
        )
        self.client.force_authenticate(user=self.user)

        self.list_url = reverse('library:authors')
        self.author = Author.objects.create(
            first_name='Leo',
            last_name='Tolstoy',
            birth_date='1828-09-09',
            death_date='1910-11-20'
        )

    def test_list_authors_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['first_name'], 'Leo')

    def test_list_authors_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_author_successful(self):
        data = {
            'first_name': 'Jane',
            'last_name': 'Austen',
            'birth_date': '1775-12-16',
            'death_date': '1817-07-18'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Author.objects.filter(
            first_name='Jane', last_name='Austen').exists())

    def test_create_author_missing_field(self):
        data = {
            'first_name': 'Mark'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('last_name', response.data)
