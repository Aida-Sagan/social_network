from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {}
        fields = ['photo', 'caption', 'text']
