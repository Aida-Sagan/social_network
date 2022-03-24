from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import PostForm


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, template_name='post_create.html', context={'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
        return render(request, template_name='post_create.html', context={'form': form})
