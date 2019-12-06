from django.test import TestCase, Client
from django.urls import resolve
from jadwal.views import CalendarView

# Create your tests here.

class JadwalTest(TestCase):
    # testing whether the url exist or not
    def test_landing_url_is_exist(self):
        response = Client().get('/jadwal/')  # calling router if browser get
        self.assertEqual(response.status_code, 200)

    # test to make sure path using index function
    def test_calendar_using_template(self):
        response = Client().get('/jadwal/')
        self.assertTemplateUsed(response, 'jadwal/jadwal.html')