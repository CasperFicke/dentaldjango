### URLS.PY EVENTS APP ###

# Django
from django.urls import path, include

# local
from . import views

urlpatterns = [
  # VENUES
   path('venues/add/', views.add_venue, name="add_venue"),
  # EVENTS
  path('events/', views.all_events, name="all_events"),
  # AGENDA
  path('events/agenda/', views.agenda, name="agenda"),
  path('events/agenda/<int:year>/<str:month>/', views.agenda , name="agenda"), # path converters
]
