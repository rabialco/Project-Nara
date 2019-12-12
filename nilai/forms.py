from django import forms
from .models import mark

class isi(forms.Form):
	nama_matkul = forms.CharField(widget=forms.DateTimeInput(attrs={
		"class" : "form-control",
		"placeholder" : "Insert Subject",
		"type" : "text",
		"required" : True
	}))

	jumlah_sks = forms.IntegerField()
 
	besar_nilai = forms.ChoiceField(choices = mark.nilai_choice, widget=forms.Select(attrs={
		"class" : "form-control",
		"placeholder" : "Insert Mark",
		"required" : True
	}))

	semester_ke = forms.IntegerField()

class cari_semester(forms.Form):
	pencarian = forms.IntegerField()