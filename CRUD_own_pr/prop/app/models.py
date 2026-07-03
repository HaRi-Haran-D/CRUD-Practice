from django.db import models

# Create your models here.
class Student(models.Model):
    std_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
#     mark = models.IntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name