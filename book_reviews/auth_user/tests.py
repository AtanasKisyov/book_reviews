from django import test as django_test
from django.urls import reverse

from book_reviews.auth_user.models import Profile, AuthUser
from book_reviews.auth_user.views import DetailUserView
from book_reviews.review.tests.create_test_data_mixin import CreateTestDataMixin


class UserProfileTest(CreateTestDataMixin, django_test.TestCase):

    def test_create_profile(self):
        self.register()

        profile = Profile.objects.first()

        expected_first_name = self.valid_register_user_data['first_name']
        expected_last_name = self.valid_register_user_data['last_name']
        actual_first_name = profile.first_name
        actual_last_name = profile.last_name

        self.assertIsNotNone(profile)
        self.assertEqual(expected_first_name, actual_first_name)
        self.assertEqual(expected_last_name, actual_last_name)

    def test_create_user(self):
        self.register()

        user = AuthUser.objects.first()

        expected = self.valid_register_user_data['email']
        actual = user.email
        self.assertEqual(expected, actual)
        self.assertFalse(user.is_staff)

    def test_successful_registration_redirects_to_login(self):
        response = self.register()

        expected = self.REGISTER_SUCCESS_URL
        actual = response
        self.assertRedirects(actual, expected)

    def test_successful_login(self):
        is_logged_in = self.register_and_login()
        self.assertTrue(is_logged_in)

    def test_successful_logout(self):
        self.register_and_login()

        self.client.logout()

        user = self.get_user_data()
        self.assertTrue(user.is_anonymous)

    def test_show_correct_template_for_user_details_page(self):
        url_name = 'detail_user'
        self.register_and_login()
        user = self.get_user_data()

        response = self.client.get(reverse(url_name, kwargs={'pk': user.id}))

        expected = DetailUserView.TEMPLATE_NAME
        actual = response.context_data['template_name']
        self.assertEqual(expected, actual)

    def test_show_correct_user_for_user_details_page(self):
        url_name = 'detail_user'
        self.register_and_login()
        user = self.get_user_data()

        response = self.client.get(reverse(url_name, kwargs={'pk': user.id}))

        expected = user.id
        actual = response.context_data['profile'].user_id
        self.assertEqual(expected, actual)

    def test_edit_view_edits_profile_data(self):
        url_name = 'edit_user'
        self.register_and_login()
        user = self.get_user_data()

        self.valid_register_user_data['first_name'] = 'Gosho'
        self.client.post(
            reverse(url_name, kwargs={'pk': user.id}),
            data=self.valid_register_user_data,
        )

        user = self.get_user_data()
        profile = Profile.objects.get(pk=user.id)
        expected = self.valid_register_user_data['first_name']
        actual = profile.first_name
        self.assertEqual(expected, actual)

    def test_change_password_view__changes_password(self):
        self.register_and_login()
        user = self.get_user_data()
        change_password_data = {
            'old_password': 'unbreakable_password_1234',
            'new_password1': 'unbreakable_password_12345',
            'new_password2': 'unbreakable_password_12345',
        }
        url_name = 'change_password'
        url_kwargs = {
            'pk': user.id
        }

        response = self.client.post(
            reverse(url_name, kwargs=url_kwargs),
            data=change_password_data,
        )

        expected = 302
        actual = response.status_code
        self.assertEqual(expected, actual)
