from . import views
from django.urls import path
from .views import PostCreate

urlpatterns = [
    path('', views.start, name='start'),
    path('main/', views.main, name='main'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('like/<int:pk>/', views.liked_post, name='like_post'),
]
