from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full outline-none bg-transparent'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full outline-none bg-transparent'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full outline-none bg-transparent'
            }),
            'image': forms.URLInput(attrs={
                'class': 'w-full outline-none bg-transparent'
            }),
        }