from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test if a user with email and password is successfully created"""
        email = "random@rand.om"
        password = "random"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_with_email_normalized(self):
        """tests if the email of the user is normalized or not"""
        email = "random@RAnD.oM"
        password = "random"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_user_with_no_email_raises_error(self):
        """test if ValueError is raised if email is not provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "somePass")

    def test_create_super_user(self):
        """create a new super user (staff privilige included)"""
        user = get_user_model().objects.create_super_user(
            email="super@us.er",
            password="test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
