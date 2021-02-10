### MODELS.PY THEBLOG APP ###

# django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# python
from datetime import datetime, date

# Blogpost model
class BlogPost(models.Model):
  title     = models.CharField(max_length=200)
  title_tag = models.CharField(max_length=200, default="title")
  #snippet   = models.CharField(max_length=255)
  author    = models.ForeignKey(User, on_delete=models.CASCADE)
  body      = models.TextField()
  post_date = models.DateField(auto_now_add=True)
  category  = models.CharField(max_length=255, default='leeg')
  
  # functie om title en author in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.title + ' | ' + str(self.author)
  
  # functie om redirect url te bepalen
  def get_absolute_url(self):
    return reverse('all_blogposts')
    # return reverse('show_blogpost', args=(str(self.id)))

# Category model
class Category(models.Model):
  name = models.CharField(max_length=255)

  # functie om in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.name
  # functie om redirect url te bepalen
  def get_absolute_url(self):
    return reverse('all_blogposts')