from django.db import models


class Client(models.Model):
    username = None
    email = models.EmailField(primary_key=True, default='null@example.com')
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    cellNumber = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    dateOfBirth = models.DateField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Doctor(models.Model):
    email = models.EmailField(primary_key=True, default='null@example.com')
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.email


class Assistant(models.Model):
    email = models.EmailField(primary_key=True, default='null@example.com')
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.email
