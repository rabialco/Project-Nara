from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# from .forms import UserForm, ProfileForm
from .forms import ProfileForm
from .models import Profile
from django.core import serializers

# Create your views here.
def profil(request):
        # user_form = UserForm() #instance=request.user
        if request.user.is_authenticated:
            profile_form = ProfileForm()
            if Profile.objects.order_by('-pk')[0]:
                user = Profile.objects.order_by('-pk')[0]
                return render(request, 'profil.html', {
                    'profile_form': profile_form,
                    'nama':user.nama,
                    'username':user.username,
                    'sem':user.semester,
                    'motto':user.motto,
                })
            else:
                return render(request, 'profil.html', {
                    'profile_form': profile_form,
                })
        else:
            return redirect('landing')

def changeProfil(request):
    obj = Profile.objects.get(pk=1)
    print("masuk valid")
    obj.username = request.POST['username']
    obj.nama = request.POST['nama']
    obj.sem = request.POST['semester']
    obj.motto = request.POST['motto']
    obj.save()
    print(request.POST['motto'])
    print("Sokses")
    return HttpResponse('yey')

def getProfil(request):
    data = list(Profile.objects.values("nama","semester","username","motto"))
    return JsonResponse({"data":data}, safe=False)