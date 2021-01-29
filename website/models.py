from django.db import models

# Stock model
class Stock(models.Model):
  ticker_name = models.CharField(max_length=10)

  # register model in admin area
  def __str__(self):
    return self.ticker_name