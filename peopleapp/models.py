from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=128)
    secondname = models.CharField(max_length=128)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + ' ' + self.secondname
    