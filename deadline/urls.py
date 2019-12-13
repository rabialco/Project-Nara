from django.contrib import admin
from django.urls import path, include
from .views import index, move, unmove, erase, add_deadline_service

app_name= 'deadline'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', move, name='done'),
    path('del/<int:pk>', unmove, name='undone'),
    path('delete/<int:pk>', erase, name='erase'),
    path('add_dl_service/', add_deadline_service, name='add_dl_service')
]
