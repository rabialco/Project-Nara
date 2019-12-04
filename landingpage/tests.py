from django.test import TestCase, Client

# Create your tests here.
class LandingPageUnitTest(TestCase):
    def test_landing_page_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)