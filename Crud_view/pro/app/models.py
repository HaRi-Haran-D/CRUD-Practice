from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    occup = models.CharField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app:home')