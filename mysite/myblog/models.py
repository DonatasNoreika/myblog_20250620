from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from PIL import Image


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    title = models.CharField(verbose_name="Pavadinimas", max_length=20)
    content = HTMLField(verbose_name="Tekstas", max_length=3000)

    class Meta:
        ordering = ['-date']

    def comments_count(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(to="Post", verbose_name="Post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Tekstas", max_length=1000)

    class Meta:
        ordering = ['-date']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        min_side = min(img.width, img.height)
        left = (img.width - min_side) // 2
        top = (img.height - min_side) // 2
        right = left + min_side
        bottom = top + min_side
        img = img.crop((left, top, right, bottom))
        img = img.resize((300, 300), Image.LANCZOS)
        img.save(self.photo.path)