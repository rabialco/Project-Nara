from django.test import TestCase, Client
from django.urls import resolve
from .views import landing, tentang

# Create your tests here.
class LandingPageUnitTest(TestCase):
    def test_landing_page_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_landing_page_using_landing_views(self):
        found = resolve('/')
        self.assertEqual(found.func, landing)

    def test_landing_page_using_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'landingpage.html')

    def test_login_url_exist(self):
        response = Client().get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout_url_exist(self):
        response = Client().get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_login_using_template(self):
        response = Client().get('/login/')
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_about_page_url_exist(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_using_landing_views(self):
        found = resolve('/about/')
        self.assertEqual(found.func, tentang)