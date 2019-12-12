from django.shortcuts import render,redirect
from .forms import isi,cari_semester
from .models import mark

def masuk_data(request):
	if(request.method=="POST"):
		tmp_form = isi(request.POST)
		if(tmp_form.is_valid()):
			tmp_models = mark()
			tmp_models.mata_kuliah = tmp_form.cleaned_data["nama_matkul"]
			tmp_models.sks = tmp_form.cleaned_data["jumlah_sks"]
			tmp_models.nilai = tmp_form.cleaned_data["besar_nilai"]
			tmp_models.semester = tmp_form.cleaned_data["semester_ke"]
			tmp_models.save()
		return redirect("/nilai/")
	else:
		tmp_form = isi()
		tmk = cari_semester()
		tmp_models = mark.objects.all()
		tmp_dic = {
			"isi" : tmp_form,
			"mark" : tmp_models,
			"cari" : tmk
		}
		return render(request,"indexNilai.html", tmp_dic)

def hitung_ip(request):
	tmk = cari_semester(request.POST)
	sem = tmk.data["pencarian"]
	sem = int(sem)
	tmp = mark.objects.all()
	ss = mark
	ss = ss.objects.all().filter(semester=sem)
	ans = 0
	tmpz = 0
	jml = 0
	cnt = []
	for i in ss:
		ans += (i.sks*i.nilai)
		tmpz += i.sks
		jml += 1
		cnt.append(jml)
	if(tmpz==0):
		tmpz = 1
	ans = float(ans)/float(tmpz)
	ans = round(ans,2)
	tmp_form = isi()
	tmp_dic = {
		"isi" : tmp_form,
		"mark" : tmp,
		"ans": ans,
		"cari" : tmk,
		"tampil" : ss,
		"sem" : sem,
		"jml" : cnt
	}
	return render(request,"indexNilai.html", tmp_dic)

def reset(request):
	mark.objects.all().delete()
	tmp_form = isi()
	tmp_models = mark.objects.all()
	tmk = cari_semester()
	tmp_dic = {
		"isi" : tmp_form,
		"mark" : tmp_models,
		"cari" : tmk
	}
	return render(request,"indexNilai.html", tmp_dic)