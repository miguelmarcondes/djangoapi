from django.db import models

class Culprit(models.Model):
    name = models.CharField(max_length=200)
    race = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=200)
    description = models.CharField(max_length=500)