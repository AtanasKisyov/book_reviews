from django import test as django_test
from django.contrib.auth import get_user
from django.http import HttpRequest
from django.urls import reverse

from book_reviews.review.models import Category


class CreateTestDataMixin(django_test.TestCase):

    valid_register_user_data = {
        'email': 'test@test.com',
        'first_name': 'Pesho',
        'last_name': 'Peshov',
        'password1': 'unbreakable_password_1234',
        'password2': 'unbreakable_password_1234',

    }

    valid_login_user_data = {
        'email': 'test@test.com',
        'password': 'unbreakable_password_1234',
    }

    valid_review_data = {
        'title': 'Some Review',
        'review': 'Some content',
        'category': 'Fantasy',
    }

    REGISTER_STARTING_URL = reverse('register')
    REGISTER_SUCCESS_URL = reverse('login')
    LOGIN_STARTING_URL = reverse('login')
    LOGIN_SUCCESS_URL = reverse('home')
    CREATE_REVIEW_URL = reverse('create_review')
    HOME_URL = reverse('home')
    ALL_REVIEWS_URL = reverse('all_reviews')
    USER_REVIEWS_URL = reverse('user_reviews')
    APPROVE_REVIEWS_URL = reverse('approve_review')

    def register(self):
        return self.client.post(self.REGISTER_STARTING_URL, data=self.valid_register_user_data)

    def register_and_login(self):
        self.register()
        return self.client.login(**self.valid_login_user_data)

    def get_user_data(self):
        request = HttpRequest()
        request.session = self.client.session
        return get_user(request)

    def add_dynamic_review_data(self):
        self.register_and_login()
        category = Category.objects.create(category_name='Fantasy')
        self.valid_review_data['reviewed_by'] = self.get_user_data()
        self.valid_review_data['category'] = category.id
        return self.valid_review_data

    def create_review(self):
        self.add_dynamic_review_data()
        return self.client.post(self.CREATE_REVIEW_URL, data=self.valid_review_data)

