### URLS.PY WEBSITE APP ###

# Django
from django.urls import path, include

#from rest_framework import routers

# local
from . import views
# import views
from .views import ShowProfileView, EditProfileView, CreateProfileView

# tbv restframework
#router = routers.DefaultRouter()
#router.register('courses', views.CourseView)
#router.register('stocks', views.StockView)

urlpatterns = [
  # HOME
  path('', views.index, name="index"),

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

  # DENTO
  path('book_appointment/', views.book_appointment, name="book_appointment"),
  path('contact/', views.contact, name="contact"),
  path('about/', views.about, name="about"),
  path('blog/', views.blog, name="blog"),
  path('blog-details/', views.blog_details, name="blog-details"),
  path('pricing/', views.pricing, name="pricing"),
  path('service/', views.service, name="service"),

  # STOCKS
  path('stocks/', views.all_stocks, name="all_stocks"),
  path('stocks/<stock_id>/edit/', views.edit_stock, name="edit_stock"),
  path('stocks/<stock_id>/delete/', views.delete_stock, name="delete_stock"),
  path('stocks/values/', views.stockvalues, name="stockvalues"),

  # RESTFRAMEWORK
  #path('api/', include(router.urls))
]
