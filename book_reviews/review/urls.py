from django.urls import path

from book_reviews.review.views.comment import AddCommentView, EditCommentView, DeleteCommentView
from book_reviews.review.views.generic import HomeView, AllReviewsView, UserReviewsView, ApproveReviewView
from book_reviews.review.views.review import CreateReviewView, EditReviewView, DeleteReviewView, DetailsReviewView


urlpatterns = [
    # generic
    path('', HomeView.as_view(), name='home'),
    path('review/all', AllReviewsView.as_view(), name='all_reviews'),
    path('review/my-reviews', UserReviewsView.as_view(), name='user_reviews'),
    # review
    path('review/create/', CreateReviewView.as_view(), name='create_review'),
    path('review/edit/<int:pk>', EditReviewView.as_view(), name='edit_review'),
    path('review/delete/<int:pk>', DeleteReviewView.as_view(), name='delete_review'),
    path('review/details/<int:pk>', DetailsReviewView.as_view(), name='details_review'),
    path('review/approve/', ApproveReviewView.as_view(), name='approve_review'),
    # comment
    path('review/details/<int:pk>/comment/', AddCommentView.as_view(), name='review_comment'),
    path('review/details/comment/edit/<int:pk>', EditCommentView.as_view(), name='edit_comment'),
    path('review/details/comment/delete/<int:pk>', DeleteCommentView.as_view(), name='delete_comment'),
]
