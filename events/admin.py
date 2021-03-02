### ADMIN.PY EVENTS APP ###

# Django
from django.contrib import admin

# Local
from .models import Event, Venue, Visitor

# Register your models here.

# Register Visitor
admin.site.register(Visitor)

# Register Venue with customized admin area
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
  list_display  = ('name', 'adres', 'telefoon')
  ordering      = ('name',)
  search_fields = ('name', 'adres')

# Register Event with customized admin area
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  fields        = (('name', 'venue'), 'event_date', 'description', 'manager', 'attendees')
  list_display  = ('name', 'event_date', 'venue')
  list_filter  = ('event_date', 'venue')
  ordering      = ('event_date',)
  search_fields = ('name', 'venue')
