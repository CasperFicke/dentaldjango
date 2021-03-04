### FORMS.PY EVENTS APP ###

#Django
from django import forms
from django.forms import ModelForm

#Local
from .models import Venue

# Venue form
class VenueForm(ModelForm):
  class Meta:
    model  = Venue
    fields = ('name', 'adres', 'postcode', 'plaats', 'telefoon', 'website', 'email')
    labels  = {
      'name': 'Venue naam',
      'adres': 'adres',
      'postcode': 'postcode',
      'plaats': 'plaats',
      'telefoon': 'telefoon',
      'website': 'website',
      'email': 'e-mail'
    }
    widgets = {
      'name'     : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'naam'}),
      'adres'    : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'straatnaam huisnummer'}),
      'postcode' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234 AB'}),
      'plaats'   : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'plaatsnaam'}),
      'telefoon' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0123456789'}),
      'website'  : forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://xxx.yyy'}),
      'email'    : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'aaa@bbb.ccc'})
    }