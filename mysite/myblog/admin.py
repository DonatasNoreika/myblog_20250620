from django.contrib import admin
from .models import Post, Comment, Profile


# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'date', 'title']
    inlines = [CommentInLine]


admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
