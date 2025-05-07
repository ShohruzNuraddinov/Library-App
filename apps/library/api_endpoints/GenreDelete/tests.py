from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from apps.library.models import Genre


class GenderDeleteAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='securepassword123'
        )
        self.client.force_authenticate(user=self.user)

        self.genre = Genre.objects.create(name="Fiction")

        self.url = reverse("library:delete-genre",
                           kwargs={"pk": self.genre.pk})

    def test_delete_genre_authenticated(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Genre.objects.filter(pk=self.genre.pk).exists())

    def test_delete_genre_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_non_existent_genre(self):
        invalid_url = reverse("library:delete-genre", kwargs={"pk": 9999})
        response = self.client.delete(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
