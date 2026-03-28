from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    descri = models.CharField(max_length=100)
    image = models.URLField(max_length=500,default='https://www.foodservicerewards.com/cdn/shop/t/262/assets/fsr-placeholder.png?v=45093109498714503231652397781')
    is_availablle = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app:home')
 
class Category(models.Model):
    name = models.CharField(max_length=50)
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name