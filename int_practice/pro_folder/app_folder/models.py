from django.db import models

# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.IntegerField()
    product_price = models.DecimalField(max_digits=6,decimal_places=2)
    product_describ = models.TextField()
    product_image = models.ImageField(upload_to='product_images', default='default.png')

    def __str__(self):
        return self.product_name
