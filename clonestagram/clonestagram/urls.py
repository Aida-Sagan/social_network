"""clonestagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from django_registration.backends.one_step.views import RegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
<<<<<<< HEAD
    path(
        'register/',
        RegistrationView.as_view(),
        name='register'
    ),
    path(
        'change_password/',
        views.PasswordChangeView.as_view(
            template_name='commons/change_password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
    
=======
    path('register/',RegistrationView.as_view()),
>>>>>>> a6465f0a72fe4d1f263f4aa7b920f38ccb9ed6a9
]
