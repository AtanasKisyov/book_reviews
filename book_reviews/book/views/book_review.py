from django.urls import reverse_lazy
from django.views import generic as generic_views

from book_reviews.auth_user.models import Profile
from book_reviews.book.forms import CreateBookReviewForm, EditBookReviewForm, ApproveBookReviewForm
from book_reviews.book.models import Book


class CreateReviewView(generic_views.CreateView):
    model = Book
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
        return super(CreateReviewView, self).form_valid(form)  # Test super method without arguments

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'Add Review'
        return context


class DetailsReviewView(generic_views.UpdateView):
    model = Book
    form_class = ApproveBookReviewForm
    template_name = 'review/review_details.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'Details'
        context['is_owner'] = False
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(pk=self.request.user.id)
            context['is_owner'] = context['object'].reviewed_by == profile
        if self.request.user.is_superuser or self.request.user.is_staff:
            context['approval_button'] = ApproveBookReviewForm
        return context


class EditReviewView(generic_views.UpdateView):
    model = Book
    form_class = EditBookReviewForm
    template_name = 'review/review_edit.html'
    success_url = reverse_lazy('home')  # Change it to review details

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'Edit Review'
        return context


class DeleteReviewView(generic_views.DeleteView):
    model = Book
    template_name = 'review/review_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'Delete Review'
        return context
