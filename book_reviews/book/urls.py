from django.urls import path

from book_reviews.book.views import HomeView, CreateReviewView, EditReviewView, DeleteReviewView, DetailsReviewView, \
    AllReviewsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('review/all', AllReviewsView.as_view(), name='all_reviews'),
    path('review/create/', CreateReviewView.as_view(), name='create_review'),
    path('review/edit/int:<pk>', EditReviewView.as_view(), name='edit_review'),
    path('review/delete/int:<pk>', DeleteReviewView.as_view(), name='delete_review'),
    path('review/details/int:<pk>', DetailsReviewView.as_view(), name='details_review'),
]
