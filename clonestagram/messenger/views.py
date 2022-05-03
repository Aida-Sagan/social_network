from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.urls import reverse

from .models import Message, Chat
from .forms import ChatForm


class ChatCreate(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = ChatForm()
            users = User.objects.all()
            return render(request, 'messenger/chat_create.html', {'form': form, 'users': users})
        else:
            return redirect(reverse('login'))

    def post(self, request):
        bound_form = ChatForm(request.POST)
        if bound_form.is_valid():
            form = bound_form.save(commit=False)
            form.user = request.user
            form.is_private = False
            form.save()
            bound_form.save_m2m()
            form.members.add(request.user)
            form.save()
            return redirect(reverse('chats_list'))
        users = User.objects.all()
        return render(request, 'messenger/chat_create.html', {'form': bound_form, 'users': users})


def chats_list(request):
    chats = Chat.objects.filter(members=request.user)
    return render(request, 'messenger/chats_list.html', {'chats': chats})


def chat(request, chat_id):
    if not Chat.objects.filter(id=chat_id, members=request.user).exists():
        return redirect(reverse('chats_list'))
    messages = Message.objects.filter(chat=chat_id).order_by('created_at')
    return render(request, 'messenger/chat.html', {'chat_id': chat_id, 'messages': messages})


def private_chat(request, user_id):
    user = User.objects.get(id=user_id)
    first = min(request.user.id, user.id)
    key = str(first) + '.' + str(request.user.id + user.id - first)
    if not Chat.objects.filter(key=key).exists():
        new_chat = Chat.objects.create(
            user=request.user,
            name=user.username,
            key=key
        )
        new_chat.members.add(request.user)
        new_chat.members.add(user)
    return chat(request, chat_id=Chat.objects.get(key=key).id)
