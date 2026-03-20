from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    descri = models.CharField(max_length=100)
    image = models.CharField(max_length=500,default='https://www.foodservicerewards.com/cdn/shop/t/262/assets/fsr-placeholder.png?v=45093109498714503231652397781')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app:home')
