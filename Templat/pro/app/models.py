from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .managers import ItemManager


# Create your models here.
class Item(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['user_name','price']),
        ]
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=6,decimal_places=2, db_index=True)
    descri = models.CharField(max_length=100)
    # image = models.URLField(max_length=500,default='https://i.pinimg.com/1200x/2a/a9/b7/2aa9b7ebcb1905e441c6d486dfe3ff9d.jpg')
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = ItemManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.name + ": " + str(self.price)
    
    def get_absolute_url(self):
        return reverse('app:home')
    
    def delete(self,using=None,keep_parent=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=50)
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item, related_name="orders")

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"