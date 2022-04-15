from django.shortcuts import render, redirect
from django.views import generic as generic_views

from book_reviews.auth_user.models import Profile
from book_reviews.review.models import Review


def unauthorized(request):
    context = {
        'template_name': '401 (Unauthorized)'
    }
    return render(request, context=context, template_name='generic/401.html')


def handler404(request, *args, **argv):
    response = render(request, context={}, template_name='generic/404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, context={}, template_name='generic/404.html')
    response.status_code = 500
    return response


class HomeView(generic_views.ListView):
    TEMPLATE_NAME = 'Home'
    model = Review
    template_name = 'generic/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        context['recently_added'] = Review.objects.filter(is_approved=Review.APPROVED).order_by('-reviewed_on')[:10]
        return context


class AllReviewsView(generic_views.ListView):
    TEMPLATE_NAME = 'All Reviews'
    model = Review
    template_name = 'generic/all_reviews.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        context['object_list'] = Review.objects.filter(is_approved=Review.APPROVED)
        return context


class UserReviewsView(generic_views.ListView):
    TEMPLATE_NAME = 'My Reviews'
    paginate_by = 6
    model = Review
    template_name = 'generic/user_reviews.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.id)
        context['template_name'] = self.TEMPLATE_NAME
        context['user_reviews'] = Review.objects.filter(reviewed_by=profile)
        return context


class ApproveReviewView(generic_views.ListView):
    TEMPLATE_NAME = 'Approve Reviews'
    paginate_by = 6
    model = Review
    template_name = 'generic/waiting_approval.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        context['object_list'] = Review.objects.filter(is_approved=Review.WAITING_FOR_APPROVAL)
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff or not request.user.is_superuser:
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)
