### ADMIN.PY WBSITE APP ###

# django
from django.contrib import admin

# Register your models here.
from .models import UserProfile, Stock, Course


myModels = [UserProfile, Stock, Course]  # iterable list
admin.site.register(myModels)