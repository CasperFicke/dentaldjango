from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('courses', views.CourseView)
router.register('stocks', views.StockView)

urlpatterns = [
  # home
  path('', views.index, name="index"),
  # usermanagement
  path('login/', views.login_user, name="login"),
  path('logout/', views.logout_user, name="logout"),
  path('register/', views.register_user, name="register"),
  path('edit_profile/', views.edit_profile, name="edit_profile"),
  path('change_password/', views.change_password, name="change_password"),
  # dento
  path('book_appointment/', views.book_appointment, name="book_appointment"),
  path('contact/', views.contact, name="contact"),
  path('about/', views.about, name="about"),
  path('blog/', views.blog, name="blog"),
  path('blog-details/', views.blog_details, name="blog-details"),
  path('pricing/', views.pricing, name="pricing"),
  path('service/', views.service, name="service"),
  # stocks
  path('stockhome/', views.stockhome, name="stockhome"),
  path('add_stock/', views.add_stock, name="add_stock"),
  path('edit_stock/<stock_id>', views.edit_stock, name="edit_stock"),
  path('delete_stock/<stock_id>', views.delete_stock, name="delete_stock"),
  # calendar
  path('agenda/', views.agenda, name="agenda"),
  path('<int:year>/<str:month>/', views.kalender , name="kalender"), # path converters
  # restframework
  path('api/', include(router.urls))
]
