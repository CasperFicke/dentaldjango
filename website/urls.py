### URLS.PY WEBSITE APP ###

# Django
from django.urls import path, include

#from rest_framework import routers

# local
from . import views
# import views

urlpatterns = [
  # HOME
  path('', views.index, name="index"),

  # DENTO
  path('book_appointment/', views.book_appointment, name="book_appointment"),
  path('contact/', views.contact, name="contact"),
  path('about/', views.about, name="about"),
  path('blog/', views.blog, name="blog"),
  path('blog-details/', views.blog_details, name="blog-details"),
  path('pricing/', views.pricing, name="pricing"),
  path('service/', views.service, name="service"),

  # STOCKS
  path('stocks/', views.all_stocks, name="all_stocks"),
  path('stocks/<stock_id>/edit/', views.edit_stock, name="edit_stock"),
  path('stocks/<stock_id>/delete/', views.delete_stock, name="delete_stock"),
  path('stocks/values/', views.stockvalues, name="stockvalues"),
]
