from django import forms
from .models import mark

def getChoice():
	tmp = mark.objects.all()
	semester_choice = []
	tmpset = set()
	for i in tmp:
		tmpset.add(i.semester)

	tmp_semester = []
	for i in tmpset:
		tmp_semester.append(i)

	tmp_semester.sort()

	for i in tmp_semester:
		semester_choice.append((i, (i)))
		
	return semester_choice

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
	pencarian = forms.ChoiceField(choices = getChoice(), widget=forms.Select(attrs={
		"class" : "form-control",
		"placeholder" : "Insert Semester",
		"required" : True
	}))

	def __init__(self, *args, **kwargs):
		super(cari_semester, self).__init__(*args, **kwargs)
		self.fields['pencarian'] = forms.ChoiceField(choices=getChoice())
