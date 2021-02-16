### MODELS.PY USERS APP ###

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
