from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)