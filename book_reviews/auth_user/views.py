from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as generic_views
from book_reviews.auth_user import forms as custom_forms
from book_reviews.auth_user.models import Profile, AuthUser


class RegisterUserView(generic_views.CreateView):
    form_class = custom_forms.RegisterUserForm
    template_name = 'user_authorization/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        result = super().form_valid(form)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'user_authorization/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url


class LogoutUserView(auth_views.LogoutView):

    def get_next_page(self):
        return reverse_lazy('home')


class DetailUserView(generic_views.DetailView):
    model = Profile
    template_name = 'user_authorization/user_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        profile = Profile.objects.get(pk=user.id)
        context['profile'] = profile
        context['template_name'] = 'Profile Details'
        return context


class EditUserView(generic_views.UpdateView):
    model = Profile
    template_name = 'user_authorization/login.html'  # change this!
    fields = ('picture', 'first_name', 'last_name')
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = 'Edit Profile'
        return context


class DeleteUserView(generic_views.DeleteView):
    model = AuthUser
    template_name = 'user_authorization/delete_user.html'
    success_url = reverse_lazy('home')
