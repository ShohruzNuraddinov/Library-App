from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

User = get_user_model()


class SignupTestCase(APITestCase):
    def setUp(self):
        # Make sure your URL name matches
        self.signup_url = reverse('users:signup')

    def test_signup_successful(self):
        data = {
            'email': 'newuser@example.com',
            'password': 'strongpassword123',
            "name": "test",
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(
            email='newuser@example.com').exists())

    def test_signup_missing_fields(self):
        data = {
            'email': '',  # Missing username
            'password': 'somepass',
            "name": "test",
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_signup_duplicate_username(self):
        User.objects.create_user(email='test@example.com', password='123456')
        data = {
            'email': 'test@example.com',
            'password': 'anotherpass',
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
