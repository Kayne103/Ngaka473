from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    def __str__(self):
        return self.firstname
