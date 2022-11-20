# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Отдельная страница с постами группы
    path('posts/<slug:slug>/', views.group_posts),
]
