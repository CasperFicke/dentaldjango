### URLS.PY MAPS APP ###

# Django
from django.urls import path

# local
from . import views

urlpatterns = [
  # MAPS
  path('map/', views.default_map, name="default_map"),
]
