from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    descri = models.CharField(max_length=100)

    def __str__(self):
        return self.name