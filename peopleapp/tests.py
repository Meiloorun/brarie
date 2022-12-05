from django.test import TestCase
from django.db.backends.sqlite3.base import IntegrityError
from django.db import transaction

from .models import Person
from .forms import PersonForm
from django.urls import reverse

# Create your tests here.
class MovieTests(TestCase):
    @classmethod
    def setUpTestDate(cls):
        p1 = Person(firstname='john', secondname='smith', bio='john smith sucks')
        p1.save()
        p2 = Person(firstname='kazuya', secondname='mishima', bio='top 10 evil man')
        p2.save()

    def test_save_note(self):
        db_count = Person.objects.all().count()
        p2 = Person(firstname='jin', secondname='kazama', bio='devil man')
        p2.save()
        self.assertEqual(db_count+1, Person.objects.all().count())

    def test_duplicate_firstname(self):
        p1 = Person(firstname='heihachi', secondname='mishima', bio='top 10 evil man')
        p1.save()
        db_count = Person.objects.all().count()
        p2 = Person(firstname='heihachi', secondname='mishima', bio='top 10 evil man')
    
        #with self.assertRaises(IntegrityError):
        try:
            with transaction.atomic():
                p2.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count+1, Person.objects.all().count())
    
    def test_post_create(self):
        db_count = Person.objects.all().count()
        data = {
            'firstname': 'arnold',
            'secondname': 'sch',
            'bio': 'robot man',
        }
        response = self.client.post(reverse('peopleapp:new_person'), data=data)
        self.assertEqual(Person.objects.count(), db_count+1)
    
    def test_person_index(self):
        response = self.client.get(reverse('peopleapp:people_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Profile')
    
    def test_person_form(self):
        data = {
            'firstname': 'Ken',
            'secondname': 'Masters',
            'bio': 'american fighter',
        }

        form = PersonForm(data)
        self.assertTrue(form.is_valid())

    def test__incorrect_person_form(self):
        data = {
            'firstname': '',
            'secondname': 'Masters',
            'bio': 'american fighter',
        }

        form = PersonForm(data)
        self.assertFalse(form.is_valid())