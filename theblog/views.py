### VIEWS.PY THEBLOG APP ###

# django
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

# local
from .models import BlogPost, Category, Comment
from .forms import PostForm, UpdateForm, CommentForm

# tbv rest API's
#from rest_framework import viewsets
#from .serializers import BlogPostSerializer

##############
# CATEGORIES #
##############

# Show all blogposts
class BlogsView(ListView):
  model         = BlogPost
  template_name = 'all_blogposts.html'
  ordering      = ['-post_date']
  # ordering    = ['-id']

  # function to make data usable in html
  def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context  = super(BlogsView, self).get_context_data(*args, **kwargs)
    context["cat_menu"] = cat_menu
    return context

# Show blogpost
class BlogPostView(DetailView):
  model         = BlogPost
  template_name = 'show_blogpost.html'

  # function to make data usable in html
  def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context  = super(BlogPostView, self).get_context_data(*args, **kwargs)
    # total likes
    stuff = get_object_or_404(BlogPost, id=self.kwargs['pk'])
    total_likes = stuff.total_likes()
    
    # liked status
    liked=False
    if stuff.likes.filter(id=self.request.user.id).exists():
      liked = True
    
    context["cat_menu"] = cat_menu
    context["total_likes"] = total_likes
    context["liked"] = liked
    return context

# like blogpost
def LikeView(request, pk):
  blogpost = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
  liked = False
  if blogpost.likes.filter(id=request.user.id).exists():
    blogpost.likes.remove(request.user)
    liked = False
  else:
    blogpost.likes.add(request.user)
    liked = True
  return HttpResponseRedirect(reverse('show_blogpost', args=[str(pk)]))
    
# add blogpost
class AddBlogPostView(CreateView):
  model         = BlogPost
  form_class    = PostForm
  template_name = 'add_blogpost.html'
  # fields      = '__all__'
  # function to get userid of loggendin user and use it to assign the new blogpost to this user
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

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
#class BlogView(viewsets.ModelViewSet):
#  queryset         = BlogPost.objects.all()
#  serializer_class = BlogPostSerializer

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

############
# COMMENTS #
############

# add comment
class AddCommentView(CreateView):
  model         = Comment
  form_class    = CommentForm
  template_name = 'add_comment.html'
  # redirect to blogpost
  def get_success_url(self):
     return reverse_lazy('show_blogpost', kwargs={'pk': self.kwargs['pk']})
  # function to get userid of loggendin user and use it to save profilepage
  def form_valid(self, form):
    form.instance.blogpost_id = self.kwargs['pk']
    return super().form_valid(form)
