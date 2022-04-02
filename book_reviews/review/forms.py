from django import forms

from book_reviews.review.models import Review


class BookReviewForm(forms.ModelForm):

    class Meta:
        fields = ('title', 'review', 'cover', 'category')
        model = Review


class CreateBookReviewForm(BookReviewForm):

    class Meta(BookReviewForm.Meta):
        pass


class EditBookReviewForm(BookReviewForm):

    class Meta(BookReviewForm.Meta):
        pass


class ApproveBookReviewForm(forms.ModelForm):

    class Meta:
        fields = ('is_approved',)
        model = Review
