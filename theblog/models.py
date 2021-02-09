from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
  title     = models.CharField(max_length=200)
  title_tag = models.CharField(max_length=200, default="title")
  author    = models.ForeignKey(User, on_delete=models.CASCADE)
  body      = models.TextField()
  
  # functie om title en author in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.title + ' | ' + str(self.author)
  
  # functie om redirect url te bepalen
  def get_absolute_url(self):
    return reverse('all_blogposts')
    # return reverse('show_blogpost', args=(str(self.id)))