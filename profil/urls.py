from django.urls import path, include
from .views import profil, ubahProfil

urlpatterns = [
    path('', profil, name='profil'),
    path('chg/', ubahProfil, name='ubah'),
]