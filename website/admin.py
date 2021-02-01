from django.contrib import admin

# Register your models here.
from .models import Stock, Course


myModels = [Stock, Course]  # iterable list
admin.site.register(myModels)