### MODELS.PY EVENTS APP ###

# Django
from django.db import models
from django.contrib.auth.models import User

# Venue model
class Venue(models.Model):
  name      = models.CharField('Venue Name', max_length=255)
  adres     = models.CharField(max_length=255)
  postcode  = models.CharField('Venue Postcode', max_length=10)
  plaats    = models.CharField('Venue Plaats', max_length=100)
  telefoon  = models.CharField('Venue Telefoon', max_length=25, blank=True)
  website   = models.URLField('Venue Website', max_length=100, blank=True)
  email     = models.EmailField('Venue Email', max_length=100, blank=True)

  # functie om venue in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.name

# Visitor model
class Visitor(models.Model):
  first_name = models.CharField('Visitor FirstName', max_length=100)
  last_name  = models.CharField('Visitor LastName', max_length=100)
  telefoon   = models.CharField('Visitor Telefoon', max_length=25)
  email      = models.EmailField('Visitor Email', max_length=100)

  # functie om visitor in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.first_name + ' ' + self.last_name

# Event model
class Event(models.Model):
  name        = models.CharField('Event Name', max_length=255)
  description = models.TextField('Event Description', blank=True)
  event_date  = models.DateTimeField('Event Date')
  venue       = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
  # manager   = models.CharField(max_length=100)
  manager     = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
  attendees   = models.ManyToManyField(Visitor, blank=True)

  # functie om event in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.name
