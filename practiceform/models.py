from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    category_id = models.CharField(max_length=20)
    category_name = models.CharField(max_length=100)


class Post(models.Model):
    category_id = models.ForeignKey(
        PostCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
