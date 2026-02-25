from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'emp_list.html', {'list':list})


def update_list(request, item_id):
    item = Company.objects.get(id=item_id)
    form = CompanyForm(instance=item)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'emp_update.html', {'form': form})


def delete_list(request, item_id):
    emp = get_object_or_404(Company, id=item_id)
    if request.method == "POST":
        emp.delete()
        return redirect("list")
    return redirect("list")

