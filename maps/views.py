from django.shortcuts import render

# Create your views here.

def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoiY2ZpY2tlIiwiYSI6ImNrbGIwYzg0ajBxa2EydnM4eXR1ZHp0dGgifQ.x9EoFA_ddcBU5HkBDGZ-eA'
    return render(request, 'default_map.html', { 'mapbox_access_token': mapbox_access_token })
    