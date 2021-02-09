### VIEWS.PY THEBLOG APP ###

# django
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect


#local
from .models import BlogPost
from .forms import PostForm, UpdateForm

# Create your views here.
#def newblog(request):
#  return render (request, 'newblog.html', {})

######################
# class based views:
######################

# Blogview homepage
class BlogsView(ListView):
  model = BlogPost
  template_name = 'all_blogposts.html'

# show blogpost
class BlogPostView(DetailView):
  model = BlogPost
  template_name = 'show_blogpost.html'


# add blogpost
class AddBlogPostView(CreateView):
  model = BlogPost
  form_class = PostForm
  template_name = 'add_blogpost.html'
  # fields = '__all__'
  # fields = ('title', 'body')

# update blogpost
class UpdateBlogPostView(UpdateView):
  model = BlogPost
  form_class = UpdateForm
  template_name = 'update_blogpost.html'
  # fields = ['title', 'title_tag', 'body']

# delete post
class DeleteBlogPostView(DeleteView):
  model = BlogPost
  template_name = 'delete_blogpost.html'
  success_url = reverse_lazy('all_blogposts')