# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('posts/<slug:slug>/', views.group_posts, name='group_posts'),
    # Отдельная страница с постами группы
    # path('posts/<slug:slug>/', views.group_posts),
]
