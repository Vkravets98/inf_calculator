from django.db import models
from django.contrib.auth.models import User

class General_Information(models.Model):
    patient_id = models.IntegerField(default = 0)
    age = models.IntegerField(default = 40)
    mass = models.FloatField(default = 70)
    day_of_disease = models.IntegerField(default = 0)
    diagnosis = models.CharField(max_length=100)
    sex = models.CharField(default = 'male', max_length= 100)

class Analizes(models.Model):
    patient_id = models.IntegerField(default=0)
    temperature = models.FloatField(default = 36.6)
    breathing_rate = models.IntegerField(default = 18)
    hct = models.FloatField(default = 0.42)
    diuresis = models.IntegerField(default = 1000)
    Na = models.IntegerField(default = 140)
    K = models.FloatField(default = 4.5)
    Glu = models.FloatField(default = 5)
    Urea = models.FloatField(default = 5)
    pH = models.FloatField(default = 7.4)
    Cl = models.IntegerField(default = 102)
    BE = models.FloatField(default = 1)
    patient_indicators = models.ManyToManyField(General_Information)

class Person(models.Model):
    name = models.CharField(max_length=100)
    pe_id = models.CharField(max_length=100)
    photo = models.ImageField()

class Human(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField(default = 0)

