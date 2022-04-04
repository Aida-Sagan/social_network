from . import views
from django.urls import path
from .views import PostCreate

urlpatterns = [
    path('', views.start),
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('main', views.main)
]
