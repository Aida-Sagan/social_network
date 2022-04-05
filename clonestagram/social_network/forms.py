from django import forms
from .models import Post, Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'photo')
        widgets = {
            'caption': forms.TextInput(attrs={"class": "form-control"}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')
