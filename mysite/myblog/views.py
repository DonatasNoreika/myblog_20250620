from django.shortcuts import render
from .models import Post
from django.views import generic
from django.db.models import Q


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"


def search(request):
    query = request.GET.get('query')

    posts_search_results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(
            author__first_name__icontains=query) | Q(author__last_name__icontains=query))

    context = {
        "query": query,
        "posts": posts_search_results,
    }
    return render(request, template_name="search.html", context=context)
