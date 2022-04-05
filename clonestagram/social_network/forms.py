from django import forms
from .models import Post, Profile
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'text')
        widgets = {
            'caption': forms.TextInput(attrs={"class": "form-control"}),
            'text': forms.Textarea(attrs={"class": "form-control"}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')
