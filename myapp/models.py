# models.py

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.postgres.search import SearchVector

class Category(models.Model):
    image = models.ImageField(upload_to="category_images")
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to="blog_images")
    background_color=models.CharField(max_length=8)
    heading = models.CharField(max_length=200)
    title = models.TextField()
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    search_vector = SearchVector("title", "heading")
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector("title", "heading")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])

