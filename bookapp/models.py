from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128)
    ISBN = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey('peopleapp.Person', on_delete=models.CASCADE, default=1)
    publisher = models.CharField(max_length=128)
