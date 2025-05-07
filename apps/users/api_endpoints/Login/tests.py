from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

User = get_user_model()


class AuthLoginTestCase(APITestCase):
    def setUp(self):
        self.login_url = reverse('users:login')  # /api/token/
        self.user = User.objects.create_user(
            email='test@test.com', password='securepassword123')

    def test_login_successful(self):
        response = self.client.post(self.login_url, {
            'email': 'test@test.com',
            'password': 'securepassword123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_wrong_password(self):
        response = self.client.post(self.login_url, {
            'email': 'test@test.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_login_user_not_found(self):
        response = self.client.post(self.login_url, {
            'email': 'test2@test.com',
            'password': 'doesntmatter'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
