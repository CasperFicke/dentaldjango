### VIEWS.PY WEBSITE APP ###

# django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.core.mail import send_mail

# local
from .forms  import SignUpForm, EditProfileForm, StockForm
from .models import Stock, Course

# python packages
import os

import calendar
from calendar import HTMLCalendar, monthrange
from datetime import datetime

# tbv rest API's
from rest_framework import viewsets
from .serializers import CourseSerializer, StockSerializer

# Index view
def index(request):
  return render(request, 'index.html', {})

# Login view
def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, ('Succesfully logged in'))
      # Redirect to a success page.
      return redirect('index')
    else:
      messages.success(request, ('Error logging in. Please try again..'))
      return redirect('login')
  else:
    return render(request, 'authenticate/login.html', {})

# Logout view
def logout_user(request):
  logout(request)
  messages.success(request, ('Succesfully logged out'))
  # Redirect to a success page.
  return redirect('index')

# Register view
def register_user(request):
  if request.method == 'POST':
    #do something
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(request, username=username, password=password)
      login(request, user)
      messages.success(request, ("You're Registered"))
      return redirect('index')
  else:
    form = SignUpForm()
  context = {'form': form}
  return render(request, 'authenticate/register.html', context)

# edit profile view
def edit_profile(request):
  if request.method == "POST":
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      messages.success(request, ("You successfully updated your profile"))
      return redirect('index')
  else:
    form = EditProfileForm(instance=request.user)
  context = {'form': form}
  return render(request, 'authenticate/edit_profile.html', context)

# change password view
def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(data=request.POST, user=request.user)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      messages.success(request, ("You successfully changed your password"))
      return redirect('index')
  else:
    form = PasswordChangeForm(user=request.user)
  context = {'form': form}
  return render(request, 'authenticate/change_password.html', context)

# contact view
def contact(request):
  # present the page after posting the form
  if request.method == "POST":
    message_name  = request.POST['message-name']
    message_email = request.POST['message-email']
    message       = request.POST['message']

    # send email
    send_mail(
      'email from website by ' + message_name, # subjext
      message, # mesage
      message_email, # from
      ['cficke@quicknet.nl'], # to
      fail_silently=False,
    )
    return render(
      request,
      'contact.html',
      {'message_name':  message_name}
    )
  else:
    # present the page
    return render(request, 'contact.html', {})

# about view
def about(request):
  return render(request, 'about.html', {})

# blog view
def blog(request):
  return render(request, 'blog.html', {})

# blog-details view
def blog_details(request):
  return render(request, 'blog-details.html', {})

# pricing view
def pricing(request):
  return render(request, 'pricing.html', {})

# service view
def service(request):
  return render(request, 'service.html', {})

# book appointment view
def book_appointment(request):
  return render(request, 'book_appointment.html', {})

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
    'events/agenda.html', {
    "year":year,
    "month": month,
    "month_number": month_number,
    "cal": cal,
    "current_time": current_time
    })

# Stockhome view
def stockhome(request):
  import requests
  import json
  iexcloud_apikey = os.getenv('IEXCLOUD_APIKEY')

  tickers = Stock.objects.all()
  output = []
  for ticker_item in tickers:
      api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) + "/quote?token=" + iexcloud_apikey)
      try:
        api_result_table = json.loads(api_request.content)
        output.append(api_result_table)
      except Exception as e:
        api_result = "Error..."  

  if request.method == "POST":
    ticker_name        = request.POST['ticker_name']
    ticker_description = request.POST['ticker_description']
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker_name + "/quote?token=" + iexcloud_apikey)
    try:
      api_result = json.loads(api_request.content)
    except Exception as e:
      api_result = "Error..."
    
    add_stock_form = StockForm(request.POST or None)

    if add_stock_form.is_valid():
      add_stock_form.save()
      messages.success(request, ("Aandeel " + ticker_name + " ; " + ticker_description + " is aan de tabel toegevoegd"))
      return redirect('stockhome')
    else:
      messages.success(request, ("Error in form ..."))

    # render page after POST
    return render(request, 'stocks/stockhome.html', {'api_result': api_result, 'output': output})
  else:
    # render page after GET
    return render(request, 'stocks/stockhome.html', {'output': output})

# add stock view
def add_stock(request):
  import json
  import requests

  tickers = Stock.objects.all()

  if request.method == "POST":
    ticker_name        = request.POST['ticker_name']
    ticker_description = request.POST['ticker_description']
    add_stock_form = StockForm(request.POST or None)
    # process formulier
    if add_stock_form.is_valid():
      add_stock_form.save()
      messages.success(request, ("Aandeel " + ticker_name + " ; " + ticker_description + " is aan de tabel toegevoegd"))
      return redirect('add_stock')
    else:
      messages.success(request, ("Error in formulier ..."))

  return render(request, 'stocks/add_stock.html', {'tickers': tickers})

# edit stock view
def edit_stock(request, stock_id):
  if request.method == 'POST':
    item = Stock.objects.get(pk=stock_id)
    form = StockForm(request.POST or None, instance=item)
    if form.is_valid():
      form.save()
      messages.success(request, ('Item updated'))
      return redirect('add_stock')
  else:
    item = Stock.objects.get(pk=stock_id)
    return render(request, 'stocks/edit_stock.html', {'item': item})

# delete stock view
def delete_stock(request, stock_id):
  item = Stock.objects.get(pk=stock_id)
  ticker_name   = item.ticker_name
  ticker_description = item.ticker_description
  item.delete()
  messages.success(request, ("Aandeel " + ticker_name + " ; " + ticker_description + " has been deleted!"))
  return redirect(add_stock)

# Course view
class CourseView(viewsets.ModelViewSet):
  queryset         = Course.objects.all()
  serializer_class = CourseSerializer

# Stock view
class StockView(viewsets.ModelViewSet):
  queryset         = Stock.objects.all()
  serializer_class = StockSerializer