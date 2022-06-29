from urllib.parse import urlparse
from django.shortcuts import render, redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

class PostsView(ListView):
    model = Post
    template_name = "index.html"

class DetailPostView(DetailView):
    model = Post
    template_name = "detail_post.html"

class CreatePostView(CreateView):
    model = Post
    template_name = "create_post.html"
    form_class = PostForm 
  

class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
