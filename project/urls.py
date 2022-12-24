
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django_telethon.urls import django_telethon_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('telegram/', django_telethon_urls()),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


