from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as generic_views

from book_reviews.auth_user.models import Profile
from book_reviews.review.forms import CreateBookReviewForm, EditBookReviewForm, ApproveBookReviewForm
from book_reviews.review.helpers import is_review_owner
from book_reviews.review.models import Review, Comment


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get_login_url(self):
        return reverse_lazy('login')


class CreateReviewView(CustomLoginRequiredMixin, generic_views.CreateView):
    TEMPLATE_NAME = 'Add Review'
    model = Review
    form_class = CreateBookReviewForm
    template_name = 'review/review_add.html'
    success_url = reverse_lazy('home')

    def get_from_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = Profile.objects.get(pk=self.request.user.id)
        form.instance.reviewed_by = user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class DetailsReviewView(generic_views.UpdateView):
    TEMPLATE_NAME = 'Review Details'
    model = Review
    form_class = ApproveBookReviewForm
    template_name = 'review/review_details.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        context['is_owner'] = False
        context['comments'] = Comment.objects.filter(review_id=self.object.id)
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(pk=self.request.user.id)
            context['is_owner'] = context['object'].reviewed_by == profile
            context['profile'] = profile
        if self.request.user.is_superuser or self.request.user.is_staff:
            context['approval_button'] = ApproveBookReviewForm
        return context


class EditReviewView(CustomLoginRequiredMixin, generic_views.UpdateView):
    TEMPLATE_NAME = 'Edit Review'
    model = Review
    form_class = EditBookReviewForm
    template_name = 'review/review_edit.html'

    def get_success_url(self):
        object_id = self.object.id
        return reverse('details_review', kwargs={'pk': object_id})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context

    def dispatch(self, request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs['pk'])
        if not is_review_owner(self.request.user, review):
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class DeleteReviewView(CustomLoginRequiredMixin, generic_views.DeleteView):
    TEMPLATE_NAME = 'Delete Review'
    model = Review
    template_name = 'review/review_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context

    def dispatch(self, request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs['pk'])
        if not is_review_owner(self.request.user, review):
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)
