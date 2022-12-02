from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 128)
    releaseDate = models.DateField()
    description = models.TextField()
    status = models.IntegerField(max_length = 1) #0 = unreleased, 1 = released
    genres = models.TextField()
    ageRating = models.TextField()
    originalLanguage = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)