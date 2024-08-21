from django.urls import path
from . import views
from django.conf import settings
from blogApp.views import *

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('update/<int:pk>/', views.blog_update, name='blog_update'),
    path('delete/<int:pk>/', views.blog_delete, name='blog_delete'),
]
