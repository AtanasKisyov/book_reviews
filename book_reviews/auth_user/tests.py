from django import test as django_test
from django.urls import reverse

from book_reviews.auth_user.models import Profile, AuthUser


class UserProfileCreateViewTest(django_test.TestCase):
    VALID_REGISTER_USER_DATA = {
        'email': 'test@test.com',
        'first_name': 'Pesho',
        'last_name': 'Peshov',
        'password1': 'unbreakable_password_1234',
        'password2': 'unbreakable_password_1234',

    }
    VALID_LOGIN_USER_DATA = {
        'email': 'test@test.com',
        'password': 'unbreakable_password_1234',
    }
    REGISTER_STARTING_URL = reverse('register')
    REGISTER_SUCCESS_URL = reverse('login')
    LOGIN_STARTING_URL = reverse('login')
    LOGIN_SUCCESS_URL = reverse('home')

    def test_create_profile(self):
        self.client.post(self.REGISTER_STARTING_URL, data=self.VALID_REGISTER_USER_DATA)

        profile = Profile.objects.first()

        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_REGISTER_USER_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_REGISTER_USER_DATA['last_name'], profile.last_name)

    def test_create_user(self):
        self.client.post(self.REGISTER_STARTING_URL, data=self.VALID_REGISTER_USER_DATA)

        user = AuthUser.objects.first()

        self.assertIsNotNone(user)
        self.assertEqual(self.VALID_REGISTER_USER_DATA['email'], user.email)
        self.assertFalse(user.is_staff)

    def test_successful_registration_redirects_to_login(self):
        response = self.client.post(self.REGISTER_STARTING_URL, data=self.VALID_REGISTER_USER_DATA)
        self.assertRedirects(response, self.REGISTER_SUCCESS_URL)

    def test_successful_login(self):
        self.client.post(self.REGISTER_STARTING_URL, data=self.VALID_REGISTER_USER_DATA)
        is_logged_in = self.client.login(**self.VALID_LOGIN_USER_DATA)
        self.assertTrue(is_logged_in)
