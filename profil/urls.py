from django.urls import path, include
from .views import profil, changeProfil, getProfil

urlpatterns = [
    path('', profil, name='profil'),
    path('chg/', changeProfil, name='ubah'),
    path('get/', getProfil, name='getProfil'),
]