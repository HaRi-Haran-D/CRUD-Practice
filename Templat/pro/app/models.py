from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    descri = models.CharField(max_length=100)
    image = models.CharField(max_length=500,default='https://www.foodservicerewards.com/cdn/shop/t/262/assets/fsr-placeholder.png?v=45093109498714503231652397781')

    def __str__(self):
        return self.name
