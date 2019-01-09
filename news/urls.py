from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('courses', views.courses, name='courses'),
    path('<int:news_details_id>', views.news_details, name='news_details'),
    path('search', views.search, name='search'),
]
