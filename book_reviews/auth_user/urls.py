from django.urls import path

from book_reviews.auth_user.views import RegisterUserView, LoginUserView, LogoutUserView, DetailUserView, EditUserView, \
    DeleteUserView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('details/int:<pk>', DetailUserView.as_view(), name='detail_user'),
    path('edit/int:<pk>', EditUserView.as_view(), name='edit_user'),
    path('delete/int:<pk>', DeleteUserView.as_view(), name='delete_user'),
    path('change-password/int:<pk>', ChangePasswordView.as_view(), name='change_password'),
]
