from django.db import models

# Create your models here.

class Appoinment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    booked_on = models.DateTimeField(auto_now=True)