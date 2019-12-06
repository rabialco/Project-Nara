from django import forms
from .models import dl

class deadlines(forms.Form):
    # class Meta:
    #     model = dl
    #     fields = ['nama_deadline']
    #     widgets = {
    #         'nama_deadline' : forms.TextInput(attrs={'placeholder':'Type your schedule here', 'style': 'border:0; width:100%'})
    #     }
    daftar_deadline = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your schedule here',
        'type' : 'text',
        'maxlength' : '25',
        'required' : True,
    }))