from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
]