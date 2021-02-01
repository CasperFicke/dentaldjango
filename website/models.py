from django.db import models

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
