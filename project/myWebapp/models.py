import email
from django.db import models

# Create your models here.
class formdetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contactnum = models.CharField(max_length=10)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100)

