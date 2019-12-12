from django.urls import path, include
from .views import profil

urlpatterns = [
    path('', profil, name='profil'),
]