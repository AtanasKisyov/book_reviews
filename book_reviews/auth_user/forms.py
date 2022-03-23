from django.contrib.auth import forms as auth_forms, get_user_model
from django.forms import forms

from book_reviews.auth_user.models import Profile, AuthUser

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name')

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        return self.cleaned_data['last_name']

    def save(self, commit=True):
        user = AuthUser(
            email=self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password1'])

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        if commit:
            profile.save()
            user.save()
        return user
