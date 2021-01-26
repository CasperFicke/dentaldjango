from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('login/', views.login_user, name="login"),
  path('logout/', views.logout_user, name="logout"),
  path('register/', views.register_user, name="register"),
  path('edit_profile/', views.edit_profile, name="edit_profile"),
  path('change_password/', views.change_password, name="change_password"),
  path('book_appointment/', views.book_appointment, name="book_appointment"),
  path('contact/', views.contact, name="contact"),
  path('about/', views.about, name="about"),
  path('blog/', views.blog, name="blog"),
  path('blog-details/', views.blog_details, name="blog-details"),
  path('pricing/', views.pricing, name="pricing"),
  path('service/', views.service, name="service"),
]
