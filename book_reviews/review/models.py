from django.db import models
from book_reviews.auth_user.models import Profile


class Category(models.Model):

    CATEGORY_NAME_MAX_LENGTH = 50

    category_name = models.CharField(
        max_length=50,
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
    )

    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    cover = models.ImageField()
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
    content = models.TextField()
    commented_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE
    )
