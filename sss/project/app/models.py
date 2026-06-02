from django.db import models

# Create your models here.
class Stud(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {int(self.age)}"