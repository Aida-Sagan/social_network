from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, label="Имя пользователя", widget=forms.TextInput(attrs= {"class" : "form-control", "placeholder" : "Введите имя"})) 
    email = forms.EmailField(label="Адрес электронной почты", widget=forms.EmailInput(attrs= {"class" : "form-control", "placeholder" : "Укажите верный электронный адрес"}))
    password1 = forms.CharField(max_length=30, label="Введите пароль", widget=forms.PasswordInput(attrs= {"class" : "form-control", "placeholder" : "Придумать пароль больше 8 символов"}))
    password2 = forms.CharField(max_length=30, label="Повторите пароль", widget=forms.PasswordInput(attrs= {"class" : "form-control", "placeholder" : "Придумать пароль больше 8 символов"}))

    class Meta():
        model = User
        fields = ("username", "email", "password1", "password2")

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=30, label="Имя пользователя", widget=forms.TextInput(attrs= {"class" : "form-control", "placeholder" : "Введите имя"}))
    password = forms.CharField(max_length=30, label="Введите пароль", widget=forms.PasswordInput(attrs= {"class" : "form-control", "placeholder" : "Введите пароль"}))

class UserPasswordChangeForm(PasswordChangeForm):
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("Your old password was entered incorrectly. " "Please enter it again."),})
    old_password = forms.CharField(max_length=30, label=_("Введите свой старый пароль"), widget=forms.PasswordInput)
    new_password1 = forms.CharField(max_length=30, label=_("Введите новый пароль"), widget=forms.PasswordInput(attrs= {"class" : "form-control", "placeholder" : "Придумать пароль больше 8 символов"})))
    new_password2 = forms.CharField(label=_("Повторите новый пароль"), widget=forms.PasswordInput)
