from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy, reverse
from django.views import generic as generic_views
from book_reviews.auth_user import forms as custom_forms
from book_reviews.auth_user.forms import ChangePasswordForm
from book_reviews.auth_user.models import Profile, AuthUser


UserModel = get_user_model()


class RegisterUserView(generic_views.CreateView):
    form_class = custom_forms.RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        result = super().form_valid(form)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url


class LogoutUserView(auth_views.LogoutView):

    def get_next_page(self):
        return reverse_lazy('home')


class DetailUserView(generic_views.DetailView):
    TEMPLATE_NAME = 'Profile Details'
    model = Profile
    template_name = 'user/user_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        profile = Profile.objects.get(pk=user.id)
        context['profile'] = profile
        context['template_name'] = self.TEMPLATE_NAME
        return context


class EditUserView(generic_views.UpdateView):
    TEMPLATE_NAME = 'Edit Profile'
    model = Profile
    template_name = 'user/edit_user.html'
    success_url = reverse_lazy('home')
    fields = ('picture', 'first_name', 'last_name')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class DeleteUserView(generic_views.DeleteView):
    model = AuthUser
    template_name = 'user/delete_user.html'
    success_url = reverse_lazy('home')


class ChangePasswordView(generic_views.UpdateView):
    TEMPLATE_NAME = 'Change Password'
    model = UserModel
    form_class = ChangePasswordForm
    fields = '__all__'
    template_name = 'user/change_password.html'

    def get_form_class(self):
        return self.form_class

    def get_success_url(self):
        kwargs = {'pk': self.request.user.id}
        return reverse('detail_user', kwargs=kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.pop('instance')
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context
