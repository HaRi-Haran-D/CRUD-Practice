from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm

# Create your views here.
def home(request):
    pass

def emp_list(request):
    list = Company.objects.all()
    return(request, 'base.html', {'list':list})