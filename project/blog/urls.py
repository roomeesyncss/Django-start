from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


#In navigation bar
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/blog', views.about,name='blog-about')
]
