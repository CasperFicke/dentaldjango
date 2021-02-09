# django
from django.contrib import admin

# lokaal
from .models import BlogPost

# Register your models here.
admin.site.register(BlogPost)