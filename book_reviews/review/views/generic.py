from django.views import generic as generic_views

from book_reviews.auth_user.models import Profile
from book_reviews.review.models import Review


class HomeView(generic_views.ListView):
    model = Review
    template_name = 'generic/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'Home'
        context['recently_added'] = Review.objects.filter(is_approved=Review.APPROVED).order_by('-reviewed_on')[:10]
        return context


class AllReviewsView(generic_views.ListView):
    model = Review
    template_name = 'generic/all_reviews.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'All Reviews'
        context['object_list'] = Review.objects.filter(is_approved=Review.APPROVED)
        return context


class UserReviewsView(generic_views.ListView):
    paginate_by = 6
    model = Review
    template_name = 'generic/user_reviews.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.id)
        context['template_name'] = 'My Reviews'
        context['user_reviews'] = Review.objects.filter(reviewed_by=profile)
        return context


class ApproveReviewView(generic_views.ListView):
    paginate_by = 6
    model = Review
    template_name = 'generic/waiting_approval.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'Approve Reviews'
        context['object_list'] = Review.objects.filter(is_approved=Review.WAITING_FOR_APPROVAL)
        return context
