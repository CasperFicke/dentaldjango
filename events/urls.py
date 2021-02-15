### URLS.PY EVENTS APP ###

# Django
from django.urls import path, include

# local
from . import views

urlpatterns = [
  # AGENDA
  path('events/agenda/', views.agenda, name="agenda"),
  path('events/agenda/<int:year>/<str:month>/', views.agenda , name="agenda"), # path converters
]
