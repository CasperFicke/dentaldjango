### URLS.PY THEBLOG APP ###

from django.urls import path
#from . import views

# import views
from .views import BlogsView, BlogPostView, AddBlogPostView,UpdateBlogPostView, DeleteBlogPostView

urlpatterns = [
  #path('newblog/', views.newblog, name="newblog"),
  # show all blogposts
  path ('blogs/', BlogsView.as_view(), name='all_blogposts'),
  # show single blogpost url
  path ('blogpost/<int:pk>', BlogPostView.as_view(), name='show_blogpost'),
  # add blogpost
  path ('add_blogpost/', AddBlogPostView.as_view(), name='add_blogpost'),
  # edit blogpost
  path('blogpost/edit/<int:pk>', UpdateBlogPostView.as_view(), name='update_blogpost'),
  # delete post
   path('blogpost/<int:pk>', DeleteBlogPostView.as_view(), name='delete_blogpost'),
]
