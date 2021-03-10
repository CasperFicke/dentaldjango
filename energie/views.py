### VIEWS.PY ENERGIE APP ###

# Django
from django.core.paginator import Paginator
from django.shortcuts import render

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import io
import urllib, base64

# Local
from .models import Meterstand, Meter

from datetime import datetime, timedelta

# All Meterstanden view (function based)
# (/meterstanden/ is standen van alle meters, /meterstanden/medium/ is meterstanden van ingevoerd medium)
def all_meterstanden(request, medium='alle'):
  meterstanden_list = Meterstand.objects.all()
  
  # select standen van een gekozen medium
  medium_list = []
  if medium != 'alle':
    for item in meterstanden_list:
      if item.meter.medium == medium:
        medium_list.append(item)
    meterstanden_list = medium_list
  
  sorted_list = sorted(meterstanden_list, key=lambda meterstand: meterstand.meterstand_date, reverse=False)
  dates_list = []
  value_list = []
  for item in sorted_list:
    dates_list.append(item.meterstand_date)
    value_list.append(item.meterstand_waarde)
  
  x = dates_list
  y = value_list

  # set firstletter of medium to uppercase
  medium = medium.capitalize()

  fig, ax = plt.subplots()
  fig.suptitle(medium)
  # (1, 1, 1) staat voor lokatie van de figuur op het werkblad; (aantal rijen, aantal kolommen, plaats van het figuur)
  #axes = figure.add_subplot(1, 1, 1)
  #axes.set_ylim(0,100)
  ax.set_xlabel('datum')
  #ax.set_ylabel(meter.eenheid)
  # format date on X-axis
  plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
  # set interval to 1 month on x-axis
  plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
  # plot graph
  ax.plot(x,y, 'tab:orange')
  # rotates and right aligns the x labels, and moves the bottom of the axes up to make room for them
  fig.autofmt_xdate()

  # convert graph into string buffer and then we convert 64 bit code into image
  buf = io.BytesIO()
  fig.savefig(buf,format='png')
  buf.seek(0)
  string = base64.b64encode(buf.read())
  uri =  urllib.parse.quote(string)

  paginator = Paginator(sorted_list, 10) # Show 10 meterstanden per page.

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request,
    'all_meterstanden.html', {
    'page_obj': page_obj,
    'medium': medium,
    'data': uri,
    })
  # return  render(request, 'all_meterstanden.html', {'meterstanden_list': meterstanden_list})
