from django.db import models

# Create your models here.
class Series(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField()
    originalLanguage = models.CharField(max_length=128)
    status = models.IntegerField() #0 = upcoming, 1 = releasing, 2 = complete, 3 = returning
    genres = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Season(models.Model):
    seasonNumber = models.IntegerField()
    title = models.CharField(max_length = 128)
    description = models.TextField()
    year = models.IntegerField()
    status = models.IntegerField() #0 = upcoming, 1 = releasing, 2 = complete
    series = models.ForeignKey('Series', on_delete = models.CASCADE, related_name='seasons')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Episode(models.Model):
    episodeNumber = models.IntegerField()
    title = models.CharField(max_length = 128)
    description = models.TextField()
    date = models.DateTimeField()
    season = models.ForeignKey('Season', on_delete = models.CASCADE, related_name='episodes')
    director = models.ForeignKey('peopleapp.Person', on_delete = models.CASCADE, related_name='tvdirector', default=1)
    writer = models.ForeignKey('peopleapp.Person', on_delete = models.CASCADE, related_name='tvwriter', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)