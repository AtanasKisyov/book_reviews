from django import test as django_test
from django.urls import reverse


class ReviewTest(django_test.TestCase):

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

    CREATE_REVIEW_URL = reverse('create_review')

    def test_create_view_not_available_for_non_authenticated_users(self):
        # Implement this logic
        pass

    def test_create_review__creates_review(self):
        pass

    def test_edit_review_not_available_for_non_owner_users(self):
        # Implement this logic
        pass

    def test_edit_review__edits_review(self):
        pass

    def test_delete_review_not_available_for_non_owner_users(self):
        # Implement this logic
        pass

    def test_delete_review__deletes_review(self):
        pass

    def test_review_details_shows_correct_data(self):
        pass
