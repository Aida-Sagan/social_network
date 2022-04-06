from django import forms
from .models import Post, Profile, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'photo')
        widgets = {
            'caption': forms.TextInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={"class": "form-control", "id": "comment", "required": "True", }),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'birth_date', 'country')
