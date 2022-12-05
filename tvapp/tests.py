from django.test import TestCase
from django.db.backends.sqlite3.base import IntegrityError
from django.db import transaction

from .models import Series, Season, Episode
from .forms import SeriesForm, SeasonForm, EpisodeForm
from peopleapp.models import Person
from django.urls import reverse

# Create your tests here.
class TVTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        se1 = Series(title='series', description='This is the description', status='2', genres='Action', originalLanguage='English')
        se1.save()
        
    def test_save(self):
        db_count = Episode.objects.all().count()
        p1 = Person(firstname='josh', secondname='smith', bio='john smith sucks')
        p1.save()
        p2 = Person(firstname='jin', secondname='kazama', bio='top 10 evil man')
        p2.save()

        se2 = Series(title='series2',description='This is the description', status='1', genres='Action', originalLanguage='English')
        se2.save()

        sa = Season(seasonNumber='1', title='season', description='this is the desc', year='2019', status='1', series=se2)
        sa.save()

        ep = Episode(episodeNumber='1', title='episode', description='stuff happens', date='2019-04-21 14:00', season=sa, director=p1, writer=p2)
        ep.save()
        self.assertEqual(db_count+1, Episode.objects.all().count())

    def test_duplicate_title(self):
        se = Series(title='series2',description='This is the description', status='1', genres='Action', originalLanguage='English')
        se.save()
        db_count = Series.objects.all().count()
        
        se2 = Series(title='series2',description='This is the description', status='1', genres='Action', originalLanguage='English')
        #with self.assertRaises(IntegrityError):
        try:
            with transaction.atomic():
                se2.save()
        except IntegrityError:
            pass
        self.assertNotEqual(db_count+1, Series.objects.all().count())

    def test_post_create(self):
        db_count = Series.objects.all().count()
        data = {
            'title': 'series4',
            'description': 'New desc',
            'status': '0',
            'genres': 'romance',
            'originalLanguage': 'French'
        }
        response = self.client.post(reverse('tvapp:new_series'), data=data)
        self.assertEqual(Series.objects.count(), db_count+1)

    def test_tv_library(self):
        response = self.client.get(reverse('tvapp:tv_library'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title')
        self.assertContains(response, 'Profile')
    
    def test_form(self):
        data = {
            'title': 'series5',
            'description': 'New desc',
            'status': '0',
            'genres': 'romance',
            'originalLanguage': 'French'
        }

        form = SeriesForm(data)
        self.assertTrue(form.is_valid())

    def test_incorrect_form(self):
        data = {
            'title': '',
            'description': 'New desc',
            'status': '0',
            'genres': 'romance',
            'originalLanguage': 'French'
        }

        form = SeriesForm(data)
        self.assertFalse(form.is_valid())