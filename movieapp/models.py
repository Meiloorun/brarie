from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 128)
    releaseDate = models.DateField()
    description = models.TextField()
    status = models.IntegerField() #0 = unreleased, 1 = theatrically released, 2 = digitally released
    genres = models.TextField()
    ageRating = models.TextField()
    director = models.ForeignKey('peopleapp.Person', on_delete = models.CASCADE, related_name='filmdirector', default=1)
    writer = models.ForeignKey('peopleapp.Person', on_delete = models.CASCADE, related_name='filmwriter', default=1)
    originalLanguage = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)