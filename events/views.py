### VIEWS.PY EVENTS APP ###
# function based

# Django
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect

# local
from .models import Venue, Event
from .forms import VenueForm
import calendar
from calendar import HTMLCalendar, monthrange
from datetime import datetime

# add venue
def add_venue(request):
  submitted = False
  if request.method == "POST":
    form = VenueForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/venues/add?submitted=True')
  else:
    form = VenueForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, 'add_venue.html', {'form':form, 'submitted':submitted})

# All Events view
def all_events(request):
  event_list = Event.objects.all()
  return  render(request, 'all_events.html', {'event_list': event_list})

# agenda view (/agenda/ is huidige maand, /agenda/jaar/maand/ is ingevoerde maand)
def agenda(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
  # get current time
  now=datetime.now()
  current_time = now.strftime('%H:%M:%S')

  # set firstletter of month to uppercase
  month = month.capitalize()
  # convert month from name to number
  month_number = list(calendar.month_name).index(month)
  # make sure it's an integer
  month_number = int(month_number)

  # Create kalender
  cal = HTMLCalendar().formatmonth(
    year,
    month_number
  )
  return render(request,
    'agenda.html', {
    "year":year,
    "month": month,
    "month_number": month_number,
    "cal": cal,
    "current_time": current_time
    })
