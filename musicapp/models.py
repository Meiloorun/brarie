from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=128)
    releasedate = models.DateTimeField()
    artist = models.ManyToManyField('peopleapp.Person')
    mode = models.IntegerField() #0 = Single, 1 = E.P., 3 = Album, 4 = Collection

class Song(models.Model):
    title = models.CharField(max_length=128)
    artists = models.ManyToManyField('peopleapp.Person', related_name='artists')
    producers = models.ManyToManyField('peopleapp.Person', related_name='producers')
    writers = models.ManyToManyField('peopleapp.Person', related_name='songwriters')
    length = models.IntegerField() #length of song in minutes
    Album = models.ForeignKey(Album, on_delete = models.CASCADE)