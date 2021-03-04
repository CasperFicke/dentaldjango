### MODELS.PY ENERGIE APP ###

# Django
from django.db import models
from django.contrib.auth.models import User

# Meter model
class Meter(models.Model):
  name        = models.CharField('Meter Name', max_length=100, unique=True)
  medium      = models.CharField('Meter Medium', max_length=100)
  eenheid     = models.CharField('Meter Eenheid', max_length=10)
  description = models.CharField(max_length=255, blank=True)
  metertype   = models.CharField('Meter type', max_length=100, blank=True)

  # functie om meter in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.name

# Meterstand model
class Meterstand(models.Model):
  meter             = models.ForeignKey(Meter, blank=True, null=True, on_delete=models.CASCADE)
  meterstand_date   = models.DateTimeField('Meterstand Date')
  meterstand_waarde = models.FloatField('Meterstand Waarde')
  opnemer           = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

   # functie om meterstand in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return str(self.meter)