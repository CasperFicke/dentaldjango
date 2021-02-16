### URLS.PY USERS APP ###

# Django
from django.urls import path, include

#from rest_framework import routers

# local
from . import views
# import views
from .views import ShowProfileView, EditProfileView, CreateProfileView

urlpatterns = [
  # USER
  path('users/login/', views.login_user, name="login"),
  path('users/logout/', views.logout_user, name="logout"),
  path('users/register/', views.register_user, name="register"),
  path('users/edit_settings/', views.edit_usersettings, name="edit_usersettings"),
  path('users/change_password/', views.change_password, name="change_password"),
  # show profile page
  path('users/<int:pk>/profile/', ShowProfileView.as_view(), name='show_profile'),
  # edit profile page
  path('users/<int:pk>/edit_profile/', EditProfileView.as_view(), name='edit_profile'),
  # create profile page
  path('users/create_profile/', CreateProfileView.as_view(), name='create_profile'),
]
