from django.urls import path

from . import views

urlpatterns = [
    path('create_chat/', views.ChatCreate.as_view(), name='create_chat'),
    path('private_chat/<int:user_id>/', views.private_chat, name='private_chat'),
    path('chat/<int:chat_id>/', views.chat, name='chat'),
    path('', views.chats_list, name='chats_list'),
]
