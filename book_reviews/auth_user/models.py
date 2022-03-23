from django.contrib.auth import models as auth_models
from django.db import models

from book_reviews.auth_user import managers as custom_manager


class AuthUser(auth_models.AbstractUser, auth_models.PermissionsMixin):

    USERNAME_MAX_LENGTH = 15
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = custom_manager.BookReviewsUserManager()


class Profile(models.Model):

    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    picture = models.ImageField(
        upload_to='user_images/',
        null=True,
        blank=True,
    )

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH)

    user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
