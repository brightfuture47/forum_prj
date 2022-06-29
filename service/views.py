from urllib.parse import urlparse
from django.shortcuts import render, redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse_lazy

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

class PostsView(ListView):
    model = Post
    template_name = "index.html"
    ordering = ['-created_at']

class DetailPostView(DetailView):
    model = Post
    template_name = "detail_post.html"

class CreatePostView(CreateView):
    model = Post
    template_name = "create_post.html"
    form_class = PostForm 
  

class UpdatePostView(UpdateView):
    model = Post
    template_name = "create_post.html"
    form_class = PostForm 

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('index')
