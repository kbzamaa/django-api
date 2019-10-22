from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):
    def test_user_creation_email(self):

        email = "abc@gmail.com"
        password = "12345678"

        user = get_user_model().objects.create(
            email=email,
            password=password
        )

        # self.assertEquals(user.email, email, msg="Test fails because user email is incorrect")
        self.assertTrue(user.check_password(password))