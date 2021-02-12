### MODELS.PY WEBSITE APP ###

# Django
from django.db import models
from django.contrib.auth.models import User

# Userprofile model
class UserProfile(models.Model):
  user         = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  bio          = models.TextField()
  profile_pic  = models.ImageField(null=True, blank=True, upload_to="images/profile/")
  website_url  = models.CharField(max_length=255, null=True, blank=True)
  twitter_url  = models.CharField(max_length=255, null=True, blank=True)
  facebook_url = models.CharField(max_length=255, null=True, blank=True)

  # functie om userprofile in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return str(self.user)
  # functie om redirect url te bepalen
  def get_absolute_url(self):
    return reverse('index')


# Stock model
class Stock(models.Model):
  ticker_name        = models.CharField(max_length=10)
  ticker_description = models.CharField(max_length=200, default="")

  # register model in admin area
  def __str__(self):
    return self.ticker_name

# Course model
class Course(models.Model):
  name     = models.CharField(max_length=100)
  language = models.CharField(max_length=100)
  price    = models.CharField(max_length=20)

  # register model in admin area
  def __str__(self):
    return self.name
