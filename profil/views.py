from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import UserForm, ProfileForm
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def profil(request):
    if request.method == 'POST':
        # user_form = UserForm(request.POST) #, instance=request.user
        profile_form = ProfileForm(request.POST,request.FILES) #, instance=request.user.profile
        # if user_form.is_valid() and profile_form.is_valid():
        if profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            return redirect('profil')
    else:
        # user_form = UserForm() #instance=request.user
        profile_form = ProfileForm() #instance=request.user.profile
        if Profile.objects.order_by('-pk')[0]:
            user = Profile.objects.order_by('-pk')[0]
            return render(request, 'profil.html', {
                # 'user_form': user_form,
                'profile_form': profile_form,
                'nama':user.nama,
                'username':user.username,
                'sem':user.semester,
                'motto':user.motto,
                'foto':user.thumb
            })
        else:
             return render(request, 'profil.html', {
                'profile_form': profile_form,
             })
