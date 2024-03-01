from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about', views.aboutC, name='about'),
    path('contact', views.contact, name='contact'),
    path('email', views.email, name='email'),
    path('search/<str:cat>', views.search, name='search')


]
