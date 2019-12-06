from django.test import TestCase, Client
from django.urls import resolve
from django.http import HttpRequest
from .views import masuk_data,hitung_ip,reset
from .models import mark
# Create your tests here.
class MarkUnitCase(TestCase):
    # test url
    def test_nilai_url_is_exist(self):
        response = Client().get('/nilai/')
        self.assertEqual(response.status_code, 200)
 
    # test fungsi yang digunakan dari views
    def test_nilai_using_index_template(self):
        response = Client().get('/nilai/')
        self.assertTemplateUsed(response, 'indexNilai.html')
    
    def test_views_function(self):
        response = Client().post('/nilai/', data={'nama_matkul':'DDP', 'jumlah_sks':3, 'besar_nilai':4.0, 'semester_ke':1})
        hitung_jumlah = mark.objects.all().count()
        self.assertEqual(hitung_jumlah,1)
        response = Client().post('/nilai/hitung/', data={'pencarian':1})
        self.assertTemplateUsed(response, 'indexNilai.html')
        response = Client().post('/nilai/hapus/')
        hitung_jumlah = mark.objects.all().count()
        self.assertEqual(hitung_jumlah,0)