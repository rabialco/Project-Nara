from django.urls import path
from . import views

urlpatterns = [
	path('', views.masuk_data, name='idx'),
	path('hitung/', views.hitung_ip, name='hitung'),
	path('hapus/', views.reset, name='hapus'),
	path('getData/', views.getJSON, name='ambil'),
]