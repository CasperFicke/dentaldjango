### VIEWS.PY THEBLOG APP ###

# django
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

# local
from .models import BlogPost, Category
from .forms import PostForm, UpdateForm

# tbv rest API's
from rest_framework import viewsets
from .serializers import BlogPostSerializer

##############
# CATEGORIES #
##############

# Show all blogposts
class BlogsView(ListView):
  model         = BlogPost
  template_name = 'all_blogposts.html'
  ordering      = ['-post_date']
  # ordering     = ['-id']

  # function to make data usable in html
  def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context = super(BlogsView, self).get_context_data(*args, **kwargs)
    context["cat_menu"] = cat_menu
    return context

# Show blogpost
class BlogPostView(DetailView):
  model         = BlogPost
  template_name = 'show_blogpost.html'

# add blogpost
class AddBlogPostView(CreateView):
  model         = BlogPost
  form_class    = PostForm
  template_name = 'add_blogpost.html'
  # fields      = '__all__'
  # fields      = ('title', 'body')

# update blogpost
class UpdateBlogPostView(UpdateView):
  model         = BlogPost
  form_class    = UpdateForm
  template_name = 'update_blogpost.html'
  # fields      = ['title', 'title_tag', 'body'] (geen field in geval van gebruik form)

# delete post
class DeleteBlogPostView(DeleteView):
  model         = BlogPost
  template_name = 'delete_blogpost.html'
  success_url   = reverse_lazy('all_blogposts')

# Blog view
class BlogView(viewsets.ModelViewSet):
  queryset         = BlogPost.objects.all()
  serializer_class = BlogPostSerializer

##############
# CATEGORIES #
##############

# show all categories (functionbased view)
def CategoryListView(request):
  cat_list = Category.objects.all()
  return render(request, 'all_categories.html', {'cat_list':cat_list})

# add Category (classbased view)
class AddCategoryView(CreateView):
  model         = Category
  # form_class  = CategoryForm
  template_name = 'add_category.html'
  fields        = '__all__'
  # fields      = ('title', 'body')
 
# show all blogposts in a categorie (functionbased view)
def CategoryView(request, cats):
  category_posts = BlogPost.objects.filter(category=cats.replace('-', ' '))
  return render(
    request,
    'categories.html',
    {'cats':cats.title().replace('-', ' '),
    'category_posts': category_posts}
  )