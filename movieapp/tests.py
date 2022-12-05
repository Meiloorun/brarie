from django.test import TestCase
from django.db.backends.sqlite3.base import IntegrityError
from django.db import transaction

from .models import Movie
from peopleapp.models import Person
from django.urls import reverse

# Create your tests here.
class MovieTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        p1 = Person(firstname='john', secondname='smith', bio='john smith sucks')
        p1.save()
        p2 = Person(firstname='kazuya', secondname='mishima', bio='top 10 evil man')
        p2.save()
        m1 = Movie(title='movie', releaseDate='2002-09-27', description='This is the description', status='2', genres='Action', ageRating='15', director=p1, writer=p2, originalLanguage='English')
        m1.save()
        
    def test_save_note(self):
        db_count = Movie.objects.all().count()
        p1 = Person(firstname='josh', secondname='smith', bio='john smith sucks')
        p1.save()
        p2 = Person(firstname='jin', secondname='kazama', bio='top 10 evil man')
        p2.save()
        m2 = Movie(title='movie2', releaseDate='2002-09-27', description='This is the description', status='2', genres='Action', ageRating='15', director=p1, writer=p2, originalLanguage='English')
        m2.save()
        self.assertEqual(db_count+1, Movie.objects.all().count())

    def test_duplicate_title(self):
        db_count = Movie.objects.all().count()
        p1 = Person(firstname='james', secondname='smith', bio='john smith sucks')
        p1.save()
        p2 = Person(firstname='heihachi', secondname='mishima', bio='top 10 evil man')
        p2.save()
        m2 = Movie(title='movie2', releaseDate='2002-09-27', description='This is the description', status='2', genres='Action', ageRating='15', director=p1, writer=p2, originalLanguage='English')
        #with self.assertRaises(IntegrityError):
        try:
            with transaction.atomic():
                m2.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count+1, Movie.objects.all().count())

    def test_post_create(self):
        db_count = Movie.objects.all().count()
        data = {
            'title': 'movie2',
            'releaseDate': '3004-11-23 14:00',
            'description': 'New desc',
            'status': '0',
            'genres': 'romance',
            'ageRating': '18',
            'director': '5',
            'writer': '6',
            'originalLanguage': 'French'
        }
        response = self.client.post(reverse('movieapp:new_movie'), data=data)
        self.assertEqual(Movie.objects.count(), db_count+1)