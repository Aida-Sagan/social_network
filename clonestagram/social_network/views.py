from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import PostForm, CommentForm
from .models import Comments, Post, Profile


class PostCreate(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = PostForm()
            return render(request, template_name='blog/post_create.html', context={'form': form})
        else:
            return HttpResponseRedirect('/login')

    def post(self, request):
        bound_form = PostForm(request.POST, request.FILES)
        if bound_form.is_valid():
            bound_form = bound_form.save(commit=False)
            bound_form.user = request.user
            bound_form.save()
            return redirect('/main')
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


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, template_name='profile.html', context={'form': profile})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comments.objects.filter(post=post).order_by('created_at')
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
