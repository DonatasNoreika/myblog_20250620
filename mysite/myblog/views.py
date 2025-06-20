from django.shortcuts import render
from .models import Post
from django.views import generic


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"

