from django import forms
from .models import ModelForms

class ModelForming(forms.ModelForm):
    class Meta:
        model = ModelForms
        fields = '__all__'