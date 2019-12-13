from django.urls import path, include
from .views import profil, changeProfil, dapet

urlpatterns = [
    path('', profil, name='profil'),
    path('chg/', changeProfil, name='ubah'),
    path('get/', dapet, name='getProfil'),
]