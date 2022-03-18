from django.urls import path
from .views import PostCreate

urlpatterns = [
    path('post_create/', PostCreate.as_view(), name='post_create')
]
