# django
from django.contrib import admin

### ADMIN.PY WBSITE APP ###

# Django
from django.contrib import admin

# Local
from .models import BlogPost, Category, Comment

# Register your models here.
myModels = [BlogPost, Category, Comment]  # iterable list
admin.site.register(myModels)