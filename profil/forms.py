from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

# class UserForm(forms.ModelForm):
#     username = forms.CharField(help_text='')
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'nama', 'semester', 'motto']