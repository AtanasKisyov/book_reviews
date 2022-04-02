from django import forms

from book_reviews.review.models import Review, Comment


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


class CommentForm(forms.ModelForm):

    class Meta:
        fields = ('content', )
        model = Comment


class CreateCommentForm(CommentForm):

    class Meta(CommentForm.Meta):
        pass


class EditCommentForm(CommentForm):

    class Meta(CommentForm.Meta):
        pass
