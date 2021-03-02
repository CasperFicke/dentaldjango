### ADMIN.PY WBSITE APP ###

# Django
from django.contrib import admin

# Local
from .models import Stock, Course

# Register your models here.
myModels = [Course]  # iterable list
admin.site.register(myModels)

# Register Venue with customized admin area
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
  list_display  = ('ticker_name', 'ticker_description')
  ordering      = ('ticker_name',)
  search_fields = ('ticker_name', 'ticker_description')
