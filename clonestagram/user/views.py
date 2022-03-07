from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from .models import Post
from .forms import UserRegistrationForm, UserAuthenticationForm, UserPasswordChangeForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect("main_tape")
        else:
            messages.error(request, "Ошибка при регистрации!")
    else:
        form = UserRegistrationForm()
    context = {
        "form" : form,
    }
    return render(request, "user/registration.html", context=context)

def userLogout(request):
    logout(request)
    return redirect('clone_logout')


def userLogin(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # messages.success(request, 'Вы успешно авторизовались!')
            return redirect('clone_login')
    else:
        form = UserAuthenticationForm()
        # messages.error(request, 'Ошибка авторизации!')
    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context=context)


def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('clone_password')
        else:
            messages.error(request, 'Невозможно изменить пароль')
    else:
        form = UserPasswordChangeForm(request.user)
    context = {
        'form': form,
        'auth': not request.user.is_anonymous
    }
    return render(request, 'user/change_password.html', context=context)
