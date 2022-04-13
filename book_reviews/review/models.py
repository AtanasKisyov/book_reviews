from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from book_reviews.auth_user.models import Profile


class Category(models.Model):

    CATEGORY_NAME_MAX_LENGTH = 50

    category_name = models.CharField(
        max_length=50,
        validators=(MinLengthValidator(1),),
        unique=True,
    )

    def __str__(self):
        return self.category_name


class Review(models.Model):

    # Approval constants
    WAITING_FOR_APPROVAL = 'Waiting for approval'
    APPROVED = 'Approved'
    NOT_APPROVED = 'Not Approved'
    APPROVAL_VERBOSE_NAME = 'Approve'

    APPROVAL_CHOICES = (
        (APPROVED, APPROVED),
        (NOT_APPROVED, NOT_APPROVED),
        (WAITING_FOR_APPROVAL, WAITING_FOR_APPROVAL)
    )

    TITLE_MAX_LENGTH = 250

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=(MinLengthValidator(1),),
    )
    cover = models.ImageField(
        upload_to='review/',
        null=True,
        blank=True,
        default='review/default_review_cover.jpg'
    )
    review = models.TextField()
    reviewed_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    reviewed_on = models.DateTimeField(
        auto_now_add=True
    )
    is_approved = models.CharField(
        max_length=max([len(x) for (x, _) in APPROVAL_CHOICES]),
        choices=APPROVAL_CHOICES,
        default=WAITING_FOR_APPROVAL,
        verbose_name=APPROVAL_VERBOSE_NAME,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(validators=(MinLengthValidator(10),))
    commented_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if len(self.content) < 1:
            raise ValidationError('Your comment cannot be empty text!')
        super().save()
        return self
