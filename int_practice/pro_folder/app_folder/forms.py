from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['product_name','product_code','product_price','product_describ','product_image']