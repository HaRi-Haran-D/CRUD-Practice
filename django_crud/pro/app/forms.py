from django import forms
from .models import ModelForms

class ModelForming(forms.ModelForm):
    class Meta: 
        model = ModelForms
        fields = ['name','age','image']
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none',
            'placeholder': 'Enter Your Name'
        })
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none',
            'placeholder': 'Enter Your Age'
        })
    )

    # image = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none',
    #         'placeholder': 'Image URL'
    #     })
    # )