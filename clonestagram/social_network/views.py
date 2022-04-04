from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import Post

class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, template_name='blog/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, template_name='blog/post_create.html', context={'form': bound_form})

@login_required
def main(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'tape.html', {'posts': posts})

def start(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/main')
    else:
        return HttpResponseRedirect('/login')