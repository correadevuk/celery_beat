from django.conf.urls import include, url
from django.urls import path
from .views import HomeView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    ]