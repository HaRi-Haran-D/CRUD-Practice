from django.db import models

# Create your models here.
class ModelForms(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.CharField(max_length=500, default="https://static.thenounproject.com/png/4595376-200.png")

    def __str__(self):
        return self.name