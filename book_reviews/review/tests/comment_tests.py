from django.core.exceptions import ValidationError
from django.urls import reverse

from book_reviews.review.models import Comment, Review
from book_reviews.review.tests.create_test_data_mixin import CreateTestDataMixin
from book_reviews.review.views.comment import AddCommentView, EditCommentView, DeleteCommentView


class CommentViewTest(CreateTestDataMixin):

    def test_successful_create_comment(self):
        self.create_comment()
        comment = Comment.objects.first()

        self.assertIsNotNone(comment)

    def test_unsuccessful_create_comment(self):
        self.valid_comment_data['content'] = ''

        with self.assertRaises(ValidationError) as validation_error:
            self.create_comment()

        expected = 'Your comment cannot be empty text!'
        actual = validation_error.exception.message
        self.assertEqual(expected, actual)

    def test_edit_comment_successful(self):
        self.create_comment()
        comment = Comment.objects.first()
        self.valid_comment_data['content'] = 'Comment edited!'

        self.client.post(reverse('edit_comment', kwargs={'pk': comment.id}), data=self.valid_comment_data)
        comment = Comment.objects.first()

        expected = self.valid_comment_data['content']
        actual = comment.content
        self.assertEqual(expected, actual)

    def test_delete_comment_successful(self):
        self.create_comment()
        comment = Comment.objects.first()

        self.client.post(reverse('delete_comment', kwargs={'pk': comment.id}), data=self.valid_comment_data)

        comment = Comment.objects.first()

        self.assertIsNone(comment)

    def test_create_comment_view_shows_correct_template_name(self):
        self.create_comment()
        review = Review.objects.first()
        response = self.client.get(reverse('review_comment', kwargs={'pk': review.id}))

        expected = AddCommentView.TEMPLATE_NAME
        actual = response.context_data['template_name']

        self.assertEqual(expected, actual)

    def test_edit_comment_view_shows_correct_template_name(self):
        self.create_comment()
        comment = Comment.objects.first()
        response = self.client.get(reverse('edit_comment', kwargs={'pk': comment.id}))

        expected = EditCommentView.TEMPLATE_NAME
        actual = response.context_data['template_name']

        self.assertEqual(expected, actual)

    def test_delete_comment_view_shows_correct_template_name(self):
        self.create_comment()
        comment = Comment.objects.first()
        response = self.client.get(reverse('delete_comment', kwargs={'pk': comment.id}))

        expected = DeleteCommentView.TEMPLATE_NAME
        actual = response.context_data['template_name']

        self.assertEqual(expected, actual)
