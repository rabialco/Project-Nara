from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profil(request):
    return render(request, 'profil.html')