from django import test as django_test
from django.urls import reverse

from book_reviews.auth_user.tests import UserProfileTest
from book_reviews.review.views.generic import HomeView, AllReviewsView, UserReviewsView, ApproveReviewView


class GenericViewsTest(django_test.TestCase):

    HOME_URL = reverse('home')
    ALL_REVIEWS_URL = reverse('all_reviews')
    USER_REVIEWS_URL = reverse('user_reviews')
    APPROVE_REVIEWS_URL = reverse('approve_review')

    def test_home_page_shows_correct_template_name(self):
        response = self.client.get(self.HOME_URL)

        expected = HomeView.TEMPLATE_NAME
        actual = response.context_data['template_name']
        self.assertEqual(expected, actual)

    def test_all_reviews_view_shows_correct_template_name(self):
        response = self.client.get(self.ALL_REVIEWS_URL)

        expected = AllReviewsView.TEMPLATE_NAME
        actual = response.context_data['template_name']
        self.assertEqual(expected, actual)

    def test_user_reviews_view_shows_correct_template_name(self):
        register_url = UserProfileTest.REGISTER_STARTING_URL
        register_user_data = UserProfileTest.VALID_REGISTER_USER_DATA
        login_user_data = UserProfileTest.VALID_LOGIN_USER_DATA

        self.client.post(register_url, register_user_data)
        self.client.login(**login_user_data)
        response = self.client.get(self.USER_REVIEWS_URL)

        expected = UserReviewsView.TEMPLATE_NAME
        actual = response.context_data['template_name']
        self.assertEqual(expected, actual)

    def test_approve_reviews_view_shows_correct_template_name(self):
        response = self.client.get(self.APPROVE_REVIEWS_URL)
        expected = ApproveReviewView.TEMPLATE_NAME
        actual = response.context_data['template_name']
        self.assertEqual(expected, actual)

