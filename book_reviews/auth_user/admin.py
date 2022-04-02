from django.contrib import admin

from book_reviews.auth_user.models import Profile


@admin.register(Profile)
class RegisterProfile(admin.ModelAdmin):
    pass
