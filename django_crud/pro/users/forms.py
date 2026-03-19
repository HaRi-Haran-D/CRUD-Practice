from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    COMMON_CLASS = "w-full px-4 py-2 mt-4 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 focus:outline-none transition duration-200"

    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class':COMMON_CLASS,'placeholder':'Email Address'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        COMMON_CLASS = "w-full px-4 py-2 mt-4 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 focus:outline-none transition duration-200"

        self.fields['username'].widget.attrs['class'] = COMMON_CLASS
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = COMMON_CLASS
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = COMMON_CLASS
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''