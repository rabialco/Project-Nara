from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import resolve
from .models import dl
from .views import move, unmove, erase
# Create your tests here.
class DeadlineUnitTest(TestCase):
    def setUp(self):
        dl.objects.create(nama_deadline="deadline1")
        dl.objects.create(nama_deadline="deadline2")
    
    def test_deadline_url_is_exist(self):
        response = Client().get('/deadline/')
        self.assertEqual(response.status_code, 200)
 
    # test models
    def test_new_object_added_to_models(self):
        hitung_jumlah = dl.objects.all().count()
        self.assertEqual(hitung_jumlah,2)
 
    # test fungsi yang digunakan dari views
    def test_deadline_using_index_template(self):
        response = Client().get('/deadline/')
        self.assertTemplateUsed(response, 'deadline/index.html')
 
    def test_deadline_using_add_func(self):
        found = resolve('/deadline/1')
        self.assertEqual(found.func, move)
 
    def test_deadline_using_unmove_func(self):
        found = resolve('/deadline/del/1')
        self.assertEqual(found.func, unmove)
 
    def test_deadline_using_delete_func(self):
        found = resolve('/deadline/delete/1')
        self.assertEqual(found.func, erase)
 
    def test_can_save_a_POST_request(self):
        response = self.client.post('/deadline/', data={'daftar_deadline':'apaja'})
        hitung_jumlah = dl.objects.all().count()
        self.assertEqual(hitung_jumlah,3)
 
    def test_can_delete_an_object(self):
        response = self.client.get('/deadline/delete/1')
        hitung_jumlah = dl.objects.all().count()
        self.assertEqual(hitung_jumlah,1)