from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    
    def __str__(self)->str:
        return self.title