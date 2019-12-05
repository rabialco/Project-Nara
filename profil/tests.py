from django.test import TestCase, Client
from django.urls import resolve
from .views import profil

# Create your tests here.
class ProfileUnitTest(TestCase):
    def test_profile_url_exist(self):
        response = Client().get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_using_views(self):
        found = resolve('/profile/')
        self.assertEqual(found.func, profil)