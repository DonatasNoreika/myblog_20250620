"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    UserPostListView,
                    UserCommentListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    CommentUpdateView,
                    CommentDeleteView,
                    search,
                    register,
                    profile)

urlpatterns = [
    path("", PostListView.as_view(), name='posts'),
    path("userposts/", UserPostListView.as_view(), name='user_posts'),
    path("usercomments/", UserCommentListView.as_view(), name='user_comments'),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post"),
    path('search/', search, name='search'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path("posts/create", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("comment/<int:pk>/update", CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete", CommentDeleteView.as_view(), name="comment_delete"),

]
