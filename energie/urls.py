### URLS.PY ENERGIE APP ###

# Django
from django.urls import path, include

# local
from . import views

urlpatterns = [
  # METERSTANDEN
  path('meterstanden/', views.all_meterstanden, name="all_meterstanden"),
  path('meterstanden/<str:medium>/', views.all_meterstanden , name="all_meterstanden"), # path converter
]
