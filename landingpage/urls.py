from django.urls import path, include
from .views import landing, tentang, logout

urlpatterns = [
    path('', landing, name='landing'),
    path('about/', tentang, name='tentang'),
    path('logout/', logout, name='logout'),
]
