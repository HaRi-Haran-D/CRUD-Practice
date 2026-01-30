from django.db import models

# Create your models here.
class Student(models.Model):
    std_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True, default=None)
    phone_no = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name