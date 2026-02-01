from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['emp_id', 'emp_name', 'occupation', 'salary', 'joining_date']
