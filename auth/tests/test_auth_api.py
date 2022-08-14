from django.test import TestCase
from core.models import User
from django.urls import reverse
from rest_framework import status

class LoginViewTestCase(TestCase):

    def setUp(self):
        self.user_attrs = {
            "username": "test_user",
            "password": "pass123",
            "email": "test.user@email.com",
            "first_name": "fname",
            "paternal_last_name": "plastname",
            "is_active": True,
            "is_staff": True,
        }
        self.user = User.objects.create_user(**self.user_attrs)

    def test_login_user_successfully(self):
        """
        Login a user successfully
        """

        path = reverse("auth:system_login")
        payload = {
            "username": self.user_attrs["username"],
            "password": self.user_attrs["password"]
        }

        response = self.client.post(path, payload)
        access = response.json().get("access", "")
        refresh = response.json().get("refresh", "")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(access,'')
        self.assertNotEqual(refresh,'')

    def test_login_user_unsuccessfully(self):
        """
        Login a user unsuccessfully
        """

        path = reverse("auth:system_login")
        payload = {
            "username": "bad",
            "password": "credentials"
        }
        response = self.client.post(path, payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
