### events/admin.py ###

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
  fields        = (('name', 'venue'), 'event_start', 'event_end', 'description', 'manager', 'attendees')
  list_display  = ('name', 'event_start', 'event_end', 'venue')
  list_filter  = ('event_start', 'venue')
  ordering      = ('event_start',)
  search_fields = ('name', 'venue')
  
