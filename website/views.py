### VIEWS.PY WEBSITE APP ###

# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Local
from .forms  import  StockForm
from .models import Stock, Course

# Python packages
import os

# Index view
def index(request):
  return render(request, 'index.html', {})

### DENTO ###

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

### STOCKS ###

# Stockvalues view
def stockvalues(request):
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
      return redirect('stockvalues')
    else:
      messages.success(request, ("Error in form ..."))

    # render page after POST
    return render(request, 'stocks/stockvalues.html', {'api_result': api_result, 'output': output})
  else:
    # render page after GET
    return render(request, 'stocks/stockvalues.html', {'output': output})

# all stocks view
def all_stocks(request):
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
      return redirect('all_stocks')
    else:
      messages.success(request, ("Error in formulier ..."))

  return render(request, 'stocks/all_stocks.html', {'tickers': tickers})

# edit stock view
def edit_stock(request, stock_id):
  if request.method == 'POST':
    item = Stock.objects.get(pk=stock_id)
    form = StockForm(request.POST or None, instance=item)
    if form.is_valid():
      form.save()
      messages.success(request, ('Item updated'))
      return redirect('all_stocks')
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
  return redirect(all_stocks)

'''
 # Course view
class CourseView(viewsets.ModelViewSet):
  queryset         = Course.objects.all()
  serializer_class = CourseSerializer

# Stock view
class StockView(viewsets.ModelViewSet):
  queryset         = Stock.objects.all()
  serializer_class = StockSerializer
'''