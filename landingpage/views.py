from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
from django.urls import reverse


def landing(request):
    return render(request, 'landingpage.html')


def tentang(request):
    return render(request, 'tentang.html')


def logout(request):
    """Logs out user"""
    request.session.flush()
    return HttpResponseRedirect(reverse('landing'))
