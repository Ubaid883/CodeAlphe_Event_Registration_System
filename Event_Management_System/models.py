from django.db import models

# Create your models here.

#Registeration Model
class RegistrationModel(models.Model):
    Organization_name = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50)

   
# Event Model 
class Events(models.Model):
    title = models.ForeignKey(RegistrationModel, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    