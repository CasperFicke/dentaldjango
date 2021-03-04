### ADMIN.PY ENERGIE APP ###

# Django
from django.contrib import admin

# Local
from .models import Meter, Meterstand

# Register Meter with customized admin area
@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
  list_display  = ('name', 'medium', 'description', 'metertype')
  ordering      = ('name',)
  search_fields = ('name',)

# Register Meterstand with customized admin area
@admin.register(Meterstand)
class MeterstandAdmin(admin.ModelAdmin):
  fields        = ('meter', 'meterstand_date', 'meterstand_waarde', 'opnemer')
  list_display  = ('meter', 'meterstand_date', 'meterstand_waarde', 'opnemer')
  list_filter   = ('meterstand_date', 'opnemer')
  ordering      = ('meterstand_date',)
  search_fields = ('meter', 'opnemer',)
