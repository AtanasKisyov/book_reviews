from django.contrib import admin

from book_reviews.book.models import Category


@admin.register(Category)
class RegisterCategory(admin.ModelAdmin):
    pass
