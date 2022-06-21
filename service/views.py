from urllib.parse import urlparse
from django.shortcuts import render, redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

class PostsView(ListView):
    model = Post
    template_name = "index.html"

class DetailPostsView(DetailView):
    model = Post
    template_name = "detail_post.html"
