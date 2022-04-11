from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/', include('book_reviews.review.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('book_reviews.auth_user.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
