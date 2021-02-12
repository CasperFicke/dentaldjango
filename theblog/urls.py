### URLS.PY THEBLOG APP ###

# Django
from django.urls import path, include

from rest_framework import routers

#from . import views

# import views
from .views import BlogsView, BlogPostView, AddBlogPostView,UpdateBlogPostView, DeleteBlogPostView, BlogView, CategoryListView, AddCategoryView, CategoryView, LikeView

# tbv rest framework
router = routers.DefaultRouter()
#router.register('blogposts', BlogView.as_view({'get': 'list'}))

urlpatterns = [
  ### BLOGPOSTS ###
  # show all blogposts
  path ('blogposts/', BlogsView.as_view(), name='all_blogposts'),
  # show single blogpost
  path ('blogposts/<int:pk>', BlogPostView.as_view(), name='show_blogpost'),
  # add blogpost
  path ('blogposts/add/', AddBlogPostView.as_view(), name='add_blogpost'),
  # edit blogpost
  path('blogposts/<int:pk>/edit/', UpdateBlogPostView.as_view(), name='update_blogpost'),
  # delete post
  path('blogposts/<int:pk>/delete/', DeleteBlogPostView.as_view(), name='delete_blogpost'),

  ### CATEGORIES ###
  # show all categories
  path ('categories/', CategoryListView, name='all_categories'),
  # add category
  path ('categories/add/', AddCategoryView.as_view(), name='add_category'),
  # show all blogposts with same category
  path('categories/<str:cats>/', CategoryView, name='category'),
  
  # like a post
  path('like/<int:pk>', LikeView, name='like_post'),
    
  # restframework
  #path('api/', include(router.urls))
]
