from django.urls import path

from book_reviews.book.views.generic import HomeView, AllReviewsView, UserReviewsView, ApproveReviewView
from book_reviews.book.views.book_review import CreateReviewView, EditReviewView, DeleteReviewView, DetailsReviewView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('review/all', AllReviewsView.as_view(), name='all_reviews'),
    path('review/my-reviews', UserReviewsView.as_view(), name='user_reviews'),
    path('review/create/', CreateReviewView.as_view(), name='create_review'),
    path('review/edit/int:<pk>', EditReviewView.as_view(), name='edit_review'),
    path('review/delete/int:<pk>', DeleteReviewView.as_view(), name='delete_review'),
    path('review/details/int:<pk>', DetailsReviewView.as_view(), name='details_review'),
    path('review/approve/', ApproveReviewView.as_view(), name='approve_review'),
]
