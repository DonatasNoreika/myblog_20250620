from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    title = models.CharField(verbose_name="Pavadinimas", max_length=20)
    content = models.TextField(verbose_name="Tekstas", max_length=3000)

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    post = models.ForeignKey(to="Post", verbose_name="Post", on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Tekstas", max_length=1000)
