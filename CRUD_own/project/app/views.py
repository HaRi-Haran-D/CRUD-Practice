from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from .forms import CompanyForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            form=CompanyForm()
            messages.success(request, "Record added successfully.")
            return redirect('home')
    else:
        form = CompanyForm()
    return render(request, 'index.html', {'form': form})


def emp_list(request):
    list = Company.objects.all()
    return(request, 'emp_list.html', {'list':list})