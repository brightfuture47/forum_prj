from tkinter import Widget
from django.forms import ModelForm
from .models import Post, Comment
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "description": forms.Textarea(attrs={'class':'form-control'}),
            
        }