from django import test as django_test
from django.contrib.auth import get_user
from django.http import HttpRequest
from django.urls import reverse
from book_reviews.review.models import Review, Category
from book_reviews.review.views.review import DetailsReviewView


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
    valid_review_data = {
        'title': 'Some Review',
        'review': 'Some content',
        'category': 'Fantasy',
    }

    CREATE_REVIEW_URL = reverse('create_review')

    def add_dynamic_review_data(self):
        self.register_and_login()
        category = Category.objects.create(category_name='Fantasy')
        self.valid_review_data['reviewed_by'] = self.get_user_data()
        self.valid_review_data['category'] = category.id
        return self.valid_review_data

    def register_and_login(self):
        register_url = reverse('register')
        self.client.post(register_url, data=self.VALID_REGISTER_USER_DATA)
        return self.client.login(**self.VALID_LOGIN_USER_DATA)

    def create_review(self):
        self.add_dynamic_review_data()
        return self.client.post(self.CREATE_REVIEW_URL, data=self.valid_review_data)

    def get_user_data(self):
        request = HttpRequest()
        request.session = self.client.session
        return get_user(request)

    def test_create_view_not_available_for_non_authenticated_users(self):
        response = self.client.get(self.CREATE_REVIEW_URL)
        expected = reverse('login') + '?redirect_to=%2Freview%2Fcreate%2F'
        self.assertRedirects(response, expected)

    def test_create_review__creates_review(self):
        self.create_review()
        review = Review.objects.first()
        self.assertIsNotNone(review)
        expected = self.valid_review_data['title']
        actual = review.title
        self.assertEqual(expected, actual)

    def test_edit_review__edits_review(self):
        self.create_review()
        data_to_edit = self.valid_review_data
        data_to_edit['title'] = 'successful change!'

        review = Review.objects.first()
        self.client.post(reverse('edit_review', kwargs={'pk': review.id}), data=data_to_edit)
        review = Review.objects.first()
        expected = data_to_edit['title']
        actual = review.title
        self.assertEqual(expected, actual)

    def test_delete_review__deletes_review(self):
        self.create_review()

        review = Review.objects.first()
        self.assertIsNotNone(review)

        self.client.post(reverse('delete_review', kwargs={'pk': review.id}))
        review = Review.objects.first()
        self.assertIsNone(review)

    def test_review_details_shows_correct_data(self):
        self.create_review()
        review = Review.objects.first()
        response = self.client.get(reverse('details_review', kwargs={'pk': review.id}))

        expected_template_name = DetailsReviewView.TEMPLATE_NAME
        expected_is_owner = True
        expected_profile_id = self.get_user_data().id
        expected_object_title = review.title

        actual_template_name = response.context_data['template_name']
        actual_is_owner = response.context_data['is_owner']
        actual_profile_id = response.context_data['profile'].user_id
        actual_object_title = response.context_data['object'].title

        self.assertEqual(expected_template_name, actual_template_name)
        self.assertEqual(expected_is_owner, actual_is_owner)
        self.assertEqual(expected_profile_id, actual_profile_id)
        self.assertEqual(expected_object_title, actual_object_title)
