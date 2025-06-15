from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    
    def __str__(self)->str:
        return self.title

class Registration(models.Model):
    user= models.CharField(max_length=50)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    register_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self)->str:
        return self.user