from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):
    def test_user_creation_email(self):

        email = "abcd@gmail.com"
        password = 'djwhwivuheivbvibvebv'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # self.assertEquals(user.email, email, msg="Test fails because user email is incorrect")
        self.assertTrue(user.check_password(raw_password=password))

    def test_email_normalisation(self):
        email = 'abcd@gMAiL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='test_123'
        )

        self.assertEqual(user.email, email.lower())

    def test_email_provided(self):
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(
                email=None,
                password='test_123'
            )

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='xyz@gmail.com',
            password='test_123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
