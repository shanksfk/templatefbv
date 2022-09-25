from django import forms
from django.forms import ModelForm
from .models import Post, PostCategory


class CategoryForm(ModelForm):
    class Meta:
        model = PostCategory
        fields = "__all__"


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
