from django.db import models
from book_reviews.auth_user.models import Profile


class Category(models.Model):

    CATEGORY_NAME_MAX_LENGTH = 50

    category_name = models.CharField(
        max_length=50,
    )


class Book(models.Model):

    # Approval constants
    WAITING_FOR_APPROVAL = 'Waiting for approval'
    APPROVED = 'Approved'
    NOT_APPROVED = 'Not Approved'
    APPROVAL_VERBOSE_NAME = 'Approve'

    APPROVAL_CHOICES = (
        (APPROVED, APPROVED),
        (NOT_APPROVED, NOT_APPROVED),
    )

    # Category constants
    NOT_SPECIFIED = 'Not specified'
    FANTASY = 'Fantasy'
    EDUCATION = 'Education'
    AUTOBIOGRAPHY = 'Autobiography'
    CRIMINAL = 'Criminal'
    ROMANTIC = 'Romantic'
    SCIENCE_FICTION = 'Science Fiction'
    COMIC_BOOK = 'Comic Book'
    CLASSIC = 'Classic'
    HORROR = 'Horror'
    TITLE_MAX_LENGTH = 30

    CATEGORY_CHOICES = (
        (FANTASY, FANTASY),
        (EDUCATION, EDUCATION),
        (AUTOBIOGRAPHY, AUTOBIOGRAPHY),
        (CRIMINAL, CRIMINAL),
        (ROMANTIC, ROMANTIC),
        (SCIENCE_FICTION, SCIENCE_FICTION),
        (COMIC_BOOK, COMIC_BOOK),
        (CLASSIC, CLASSIC),
        (HORROR, HORROR),
        (NOT_SPECIFIED, NOT_SPECIFIED),
    )

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
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
