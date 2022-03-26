from django.db import models


from book_reviews.auth_user.models import Profile


class Book(models.Model):

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

    CHOICES = (
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
    category = models.CharField(
        max_length=max([len(x) for (x, _) in CHOICES]),
        choices=CHOICES,
    )
    reviewed_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
