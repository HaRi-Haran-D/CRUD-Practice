from django import forms
from .models import Company

class CompanyForm(forms.Form):
    class Meta:
        model = Company
        fields = ['emp_id', 'emp_name', 'occupation', 'salary']