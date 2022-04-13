from django.contrib import admin

from book_reviews.review.models import Category, Review, Comment


@admin.register(Category)
class RegisterCategory(admin.ModelAdmin):
    pass


@admin.register(Review)
class RegisterReview(admin.ModelAdmin):
    pass


@admin.register(Comment)
class RegisterComment(admin.ModelAdmin):
    pass
