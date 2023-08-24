from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=255, null=False, blank=False, default="example@default.com")
    username = models.CharField(max_length=30, unique=True, null=False, blank=False,default="example_username123")
    password = models.CharField(max_length=128, null=False, blank=False,default="example_password123")
    profile_picture = models.ImageField(upload_to="profile_images", null=True, blank=True)


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    blog_image = models.ImageField(upload_to="blog_images", null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
