from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as generic_views

from book_reviews.auth_user.models import Profile
from book_reviews.review.forms import CreateCommentForm, EditCommentForm
from book_reviews.review.models import Comment, Review
from book_reviews.review.views.review import CustomLoginRequiredMixin


class AddCommentView(CustomLoginRequiredMixin, generic_views.CreateView):
    TEMPLATE_NAME = 'Add Comment'
    form_class = CreateCommentForm
    template_name = 'comment/comment_add.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context

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
        url = reverse('details_review', kwargs={'pk': object_id})
        return redirect(url)


class EditCommentView(CustomLoginRequiredMixin, generic_views.UpdateView):
    TEMPLATE_NAME = 'Edit Comment'
    model = Comment
    form_class = EditCommentForm
    template_name = 'comment/comment_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context

    def get_success_url(self):
        object_id = Review.objects.get(pk=self.object.review.id).id
        kwargs = {'pk': object_id}
        return reverse('details_review', kwargs=kwargs)


class DeleteCommentView(CustomLoginRequiredMixin, generic_views.DeleteView):
    TEMPLATE_NAME = 'Delete Comment'
    model = Comment
    template_name = 'comment/comment_delete.html'

    def get_success_url(self):
        object_id = Review.objects.get(pk=self.object.review.id).id
        kwargs = {'pk': object_id}
        return reverse('details_review', kwargs=kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context
