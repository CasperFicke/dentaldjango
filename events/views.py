### events/views.py ###
# function based

# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe

# local
from .models import Venue, Event
from .forms import VenueForm
from .utils import Calendar
import calendar
from calendar import HTMLCalendar, monthrange
from datetime import datetime, timedelta, date

# Calendar view (class based)
class CalendarView(generic.ListView):
  model = Event
  template_name = 'kalender.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # use today's date for the calendar
    d = get_date(self.request.GET.get('month', None))

    # Instantiate our calendar class with today's year and date
    cal = Calendar(d.year, d.month)

    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(withyear=True)
    context['calendar'] = mark_safe(html_cal)
    context['prev_month'] = prev_month(d)
    context['next_month'] = next_month(d)
    return context

def get_date(req_month):
  if req_month:
    year, month = (int(x) for x in req_month.split('-'))
    return date(year, month, day=1)
  return datetime.today()

def prev_month(d):
  first = d.replace(day=1)
  prev_month = first - timedelta(days=1)
  month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
  return month

def next_month(d):
  days_in_month = calendar.monthrange(d.year, d.month)[1]
  last = d.replace(day=days_in_month)
  next_month = last + timedelta(days=1)
  month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
  return month

# all venues
def all_venues(request):
  venue_list = Venue.objects.all()
  return  render(request, 'all_venues.html', {'venue_list': venue_list})

# show venue
def show_venue(request, venue_id):
  venue = Venue.objects.get(pk=venue_id)
  return  render(request, 'show_venue.html', {'venue': venue})

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
