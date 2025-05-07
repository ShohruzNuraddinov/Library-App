from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserProfileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com', password='securepassword123')
        # e.g., path("profile/", ProfileView.as_view(), name="user-profile")
        self.profile_url = reverse('users:profile')
        tokens = self.user.tokens
        self.access_token = str(tokens['access'])

    def test_profile_authenticated(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_profile_unauthenticated(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
