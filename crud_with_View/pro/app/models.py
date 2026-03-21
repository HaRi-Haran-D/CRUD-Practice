from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    sub = models.CharField(max_length=40)
    clas = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:create')