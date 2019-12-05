from django.urls import path, include
from .views import landing, tentang

urlpatterns = [
    path('', landing, name='landing'),
    path('about/', tentang, name='tentang')
]