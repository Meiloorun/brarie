from django.test import TestCase

# Create your tests here.
class HomePageTests(TestCase):
    def setUp(self):
        return

    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'homepage')