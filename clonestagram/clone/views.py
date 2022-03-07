from django.shortcuts import render # noqa

# Create your views here.
def login(request):
    return render(request, 'registration/login.html', {})