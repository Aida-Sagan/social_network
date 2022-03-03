from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import Post    # noqa
from .forms import UserRegistrationForm

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
        "form": form,
    }
    return render(request, "user/registration.html", context=context)
