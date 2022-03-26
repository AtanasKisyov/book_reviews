from django import forms

from book_reviews.book.models import Book


class BookReviewForm(forms.ModelForm):

    class Meta:
        fields = ('title', 'review', 'cover', 'category')
        model = Book


class CreateBookReviewForm(BookReviewForm):

    class Meta(BookReviewForm.Meta):
        pass


class EditBookReviewForm(BookReviewForm):

    class Meta(BookReviewForm.Meta):
        pass
