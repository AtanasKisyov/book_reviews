from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from book_reviews.auth_user.models import Profile
from book_reviews.review.forms import CreateCommentForm
from book_reviews.review.models import Comment, Review


class AddCommentView(generic_views.CreateView):
    form_class = CreateCommentForm
    template_name = 'review/review_comment.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        content = self.request.POST['content']
        path = self.request.path.split('/')
        object_id = path[3].replace('int:', '')
        review = Review.objects.get(pk=object_id)
        user = Profile.objects.get(user_id=self.request.user.id)
        comment = Comment(
            content=content,
            review_id=review.id,
            commented_by=user,
        )
        comment.save()
        return redirect('home')
