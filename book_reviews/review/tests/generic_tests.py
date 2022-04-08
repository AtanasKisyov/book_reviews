from django import test as django_test

from book_reviews.review.tests.create_test_data_mixin import CreateTestDataMixin
from book_reviews.review.views.generic import HomeView, AllReviewsView, UserReviewsView, ApproveReviewView


class GenericViewsTest(CreateTestDataMixin):

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
        register_url = self.REGISTER_STARTING_URL
        register_user_data = self.valid_register_user_data
        login_user_data = self.valid_login_user_data

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
