from . import views
from django.urls import path
from .views import PostCreate

urlpatterns = [
    path('', views.start),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('profile/', views.profile, name='profile'),
    path('main', views.main)
]
