### ADMIN.PY WBSITE APP ###

# Django
from django.contrib import admin

# Local
from .models import UserProfile, Stock, Course

# Register your models here.
myModels = [UserProfile, Stock, Course]  # iterable list
admin.site.register(myModels)