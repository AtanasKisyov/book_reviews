from django.contrib.auth import get_user_model

from book_reviews.review.tests.create_test_data_mixin import CreateTestDataMixin

UserModel = get_user_model()


class ManagerTest(CreateTestDataMixin):

    def test_create_user_successful(self):
        manager = UserModel.objects
        email = self.valid_login_user_data['email']
        password = self.valid_login_user_data['password']

        user = manager.create_user(email=email, password=password)

        actual_email = user.email
        self.assertEqual(email, actual_email)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_raises(self):
        manager = UserModel.objects
        with self.assertRaises(ValueError) as value_error:
            manager.create_user(email='')

        expected = 'The given email must be set'
        actual = value_error.exception.args[0]
        self.assertEqual(expected, actual)

    def test_create_super_user_successful(self):
        manager = UserModel.objects
        email = self.valid_login_user_data['email']
        password = self.valid_login_user_data['password']

        user = manager.create_superuser(email=email, password=password)

        actual_email = user.email

        self.assertEqual(email, actual_email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_super_user_raises_value_error(self):
        manager = UserModel.objects
        email = self.valid_login_user_data['email']
        password = self.valid_login_user_data['password']
        staff_field = {'is_staff': False}
        superuser_field = {'is_superuser': False}

        with self.assertRaises(ValueError) as is_staff_value_error:
            manager.create_superuser(email=email, password=password, **staff_field)

        with self.assertRaises(ValueError) as is_superuser_value_error:
            manager.create_superuser(email=email, password=password, **superuser_field)

        expected_staff_error = 'Superuser must have is_staff=True.'
        expected_superuser_error = 'Superuser must have is_superuser=True.'
        actual_staff_error = is_staff_value_error.exception.args[0]
        actual_superuser_error = is_superuser_value_error.exception.args[0]
        self.assertEqual(expected_staff_error, actual_staff_error)
        self.assertEqual(expected_superuser_error, actual_superuser_error)
