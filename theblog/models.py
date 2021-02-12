### MODELS.PY THEBLOG APP ###

# django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# python
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Blogpost model
class BlogPost(models.Model):
  title        = models.CharField(max_length=200)
  header_image = models.ImageField(null=True, blank=True, upload_to="images/blogheader/")
  # na uitbreding van model met extra veld als er al records zijn moet default worden meegegeven. kan later weer weg.
  # title_tag  = models.CharField(max_length=255, default="default tekst")
  title_tag    = models.CharField(max_length=200, default='title')
  snippet      = models.CharField(max_length=255)
  author       = models.ForeignKey(User, on_delete=models.CASCADE)
  body         = RichTextField(blank=True, null=True)
  post_date    = models.DateField(auto_now_add=True)
  category     = models.CharField(max_length=255, default='leeg')
  likes        = models.ManyToManyField(User, related_name='blog_posts')

  # functie om aantal likes te bepalen
  def total_likes(self):
    return self.likes.count()
  
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