
from django.contrib import admin
from .models import *

# Register your models here.
# admin.py

@admin.register(Post)
class Post_Admin(admin.ModelAdmin):
    list_display = ('category', 'image','pub_date','title')
@admin.register(Category)
class Post_Admin(admin.ModelAdmin):
    list_display = ('image', 'name','desc')

# admin.site.register(Post)
