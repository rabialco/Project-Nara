from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return render(request, 'landingpage.html')

def tentang(request):
    return render(request, 'tentang.html')