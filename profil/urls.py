from django.urls import path, include
from .views import profil, changeProfil

urlpatterns = [
    path('', profil, name='profil'),
    path('chg/', changeProfil, name='ubah'),
]