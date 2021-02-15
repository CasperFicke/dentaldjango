### ADMIN.PY EVENTS APP ###

# Django
from django.contrib import admin

# Local
from .models import Event, Venue, Visitor

# Register your models here.
myModels = [Event, Venue, Visitor]
admin.site.register(myModels)