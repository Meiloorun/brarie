from django.db import models

# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length=128)
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.TextField()
    status = models.IntegerField() #0 = upcoming, 1 = currently releasing, 2 = finished
    genres = models.TextField()
    publisher = models.CharField(max_length=128)

class Issue(models.Model):
    title = models.CharField(max_length=128)
    issueno = models.IntegerField()
    releasedate = models.DateField()
    description = models.TextField()
    writer = models.ForeignKey('peopleapp.Person', on_delete = models.CASCADE, related_name='storywriter', default=1)
    illustrator = models.ForeignKey('peopleapp.Person', on_delete = models.CASCADE, related_name='illustrator', default=1)
    comic = models.ForeignKey('Comic', on_delete = models.CASCADE)