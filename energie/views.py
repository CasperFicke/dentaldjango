### VIEWS.PY ENERGIE APP ###

# Django
from django.shortcuts import render

# Local
from .models import Meterstand
from datetime import datetime

# All Meterstanden view (function based)
def all_meterstanden(request):
  meterstanden_list = Meterstand.objects.all()
  return  render(request, 'all_meterstanden.html', {'meterstanden_list': meterstanden_list})
