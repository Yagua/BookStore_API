from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from core.models import User

class BookAPITestCase(TestCase):

    def setUp(self):
        user_attrs = {
            "username": "test_user",
            "password": "test_pass",
            "email": "test@user.com",
            "first_name": "Richard",
            "paternal_last_name": "Castro",
            "is_active": True,
            "is_staff": True,
        }
        self.user = User.objects.create_user(**user_attrs)

        login_path = reverse("auth:system_login")
        response = self.client.post(login_path, {
            "username": user_attrs["username"],
            "password": user_attrs["password"]
        })
        self.access_token = response.json().get("access", '')
        self.refresh = response.json().get("refresh", '')

    def test_get_all_books_successfully(self):
        """
        Get all books in the database successfully
        """

        path = reverse("library:book_list")
        response = self.client.get(
            path,
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
