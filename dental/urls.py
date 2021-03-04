### URLS.PY DENTAL PROJECT ###

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(users/', include ('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('', include('website.urls')),
    path('', include('theblog.urls')),
    path('', include('events.urls')),
    path('', include('maps.urls')),
    path('', include('energie.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
