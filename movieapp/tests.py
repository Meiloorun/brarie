from django.test import TestCase
from django.db.backends.sqlite3.base import IntegrityError
from django.db import transaction

from .models import Movie
from .forms import MovieForm
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
        
    def test_save_movie(self):
        db_count = Movie.objects.all().count()
        p1 = Person(firstname='josh', secondname='smith', bio='john smith sucks')
        p1.save()
        p2 = Person(firstname='jin', secondname='kazama', bio='top 10 evil man')
        p2.save()
        m2 = Movie(title='movie2', releaseDate='2002-09-27', description='This is the description', status='2', genres='Action', ageRating='15', director=p1, writer=p2, originalLanguage='English')
        m2.save()
        self.assertEqual(db_count+1, Movie.objects.all().count())

    def test_duplicate_title(self):
        p1 = Person(firstname='james', secondname='smith', bio='john smith sucks')
        p1.save()
        p2 = Person(firstname='heihachi', secondname='mishima', bio='top 10 evil man')
        p2.save()
        m1 = Movie(title='movie2', releaseDate='2002-09-27', description='This is the description', status='2', genres='Action', ageRating='15', director=p1, writer=p2, originalLanguage='English')
        m1.save()
        db_count = Movie.objects.all().count()
        m2 = Movie(title='movie2', releaseDate='2002-09-27', description='This is the description', status='2', genres='Action', ageRating='15', director=p1, writer=p2, originalLanguage='English')
        #with self.assertRaises(IntegrityError):
        try:
            with transaction.atomic():
                m2.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count+1, Movie.objects.all().count())

    def test_post_create(self):
        p1 = Person(firstname='james', secondname='smith', bio='john smith sucks')
        p1.save()
        p2 = Person(firstname='heihachi', secondname='mishima', bio='top 10 evil man')
        p2.save()
        db_count = Movie.objects.all().count()
        data = {
            'title': 'movie2',
            'releaseDate': '3004-11-23 14:00',
            'description': 'New desc',
            'status': '0',
            'genres': 'romance',
            'ageRating': '18',
            'director': p1,
            'writer': p2,
            'originalLanguage': 'French'
        }
        response = self.client.post(reverse('movieapp:new_movie'), data=data)
        self.assertEqual(Movie.objects.count(), db_count+1)

    def test_movie_library(self):
        response = self.client.get(reverse('movieapp:movie_library'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title')
        self.assertContains(response, 'Profile')
    
    def test_movie_form(self):
        p1 = Person.objects.get(pk=1)
        p2 = Person.objects.get(pk=2)
        data = {
            'title': 'movie5',
            'releaseDate': '3004-11-23 14:00',
            'description': 'New desc',
            'status': '0',
            'genres': 'romance',
            'ageRating': '18',
            'director': p1,
            'writer': p2,
            'originalLanguage': 'French'
        }

        form = MovieForm(data)
        self.assertTrue(form.is_valid())

    def test__incorrect_movie_form(self):
        p1 = Person.objects.get(pk=1)
        p2 = Person.objects.get(pk=2)
        data = {
            'title': '',
            'releaseDate': '3004-11-23 14:00',
            'description': 'New desc',
            'status': '0',
            'genres': 'romance',
            'ageRating': '18',
            'director': p1,
            'writer': p2,
            'originalLanguage': 'French'
        }

        form = MovieForm(data)
        self.assertFalse(form.is_valid())
