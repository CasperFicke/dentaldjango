### events/urls.py ###

# Django
from django.urls import path, include

# local
from . import views

urlpatterns = [
  # VENUES
  path('venues/', views.all_venues, name="all_venues"),
  path('venues/<venue_id>/', views.show_venue, name="show_venue"),
  #path('venues/<venue_id>/edit/', views.edit_venue, name="edit_venue"),
  #path('venues/<venue_id>/delete/', views.delete_venue, name="delete_venue"),
  path('venues/add/', views.add_venue, name="add_venue"),
  # EVENTS
  path('events/', views.all_events, name="all_events"),
  # AGENDA
  path('events/agenda/', views.agenda, name="agenda"),
  path('events/agenda/<int:year>/<str:month>/', views.agenda , name="agenda"), # path converters
  path('events/kalender/', views.CalendarView.as_view(), name='kalender'),
]
