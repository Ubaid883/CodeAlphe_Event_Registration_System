from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)

#Registeration Model
class RegistrationModel(models.Model):
    name = models.CharField(max_length=50)
    event = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=False)
   