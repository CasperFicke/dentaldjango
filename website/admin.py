### ADMIN.PY WBSITE APP ###

# Django
from django.contrib import admin

# Local
from .models import Stock, Course

# Register your models here.
myModels = [Stock, Course]  # iterable list
admin.site.register(myModels)