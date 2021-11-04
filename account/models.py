import enum

from django.db import models


# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    cellNumber = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    dateOfBirth = models.DateField
    email = models.EmailField
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname
