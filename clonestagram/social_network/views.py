from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import PostForm


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
