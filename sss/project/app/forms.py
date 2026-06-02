from django import forms
from .models import Stud

class StudForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Stud
        fields = ['name', 'age', 'phone', 'email']