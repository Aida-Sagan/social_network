from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, label="Имя пользователя", widget=forms.TextInput(attrs= {"class" : "form-control", "placeholder" : "Введите имя"})) 
    email = forms.EmailField(label="Адрес электронной почты", widget=forms.EmailInput(attrs= {"class" : "form-control", "placeholder" : "Укажите верный электронный адрес"}))
    password1 = forms.CharField(max_length=30, label="Введите пароль", widget=forms.PasswordInput(attrs= {"class" : "form-control", "placeholder" : "Придумать пароль больше 8 символов"}))
    password2 = forms.CharField(max_length=30, label="Повторите пароль", widget=forms.PasswordInput(attrs= {"class" : "form-control", "placeholder" : "Придумать пароль больше 8 символов"}))

    class Meta():
        model = User
        fields = ("username", "email", "password1", "password2")
