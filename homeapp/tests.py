from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(TestCase):
    def setUp(self):
        return

    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'homepage')
        self.assertContains(response, 'Profile')

    def test_contact(self):
        response = self.client.get(reverse('homeapp:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact Us')
        self.assertContains(response, 'Profile')

    def test_about(self):
        response = self.client.get(reverse('homeapp:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What is this site')
        self.assertContains(response, 'Profile')
    
    def test_browse(self):
        response = self.client.get(reverse('homeapp:browse'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Movies')
        self.assertContains(response, 'Profile')