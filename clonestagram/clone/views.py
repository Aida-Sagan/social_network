from django.shortcuts import render # noqa

# Create your views here.
def check(request):
    return render(request, 'registration/check.html', {})