### ADMIN.PY USERS APP ###

# Django
from django.contrib import admin

# Local
from .models import UserProfile

# Register your models here.
myModels = [UserProfile]  # iterable list
admin.site.register(myModels)