from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form=StudentForm()
            messages.success(request, "Record added successfully.")
            return redirect('home')
    else:
        form = StudentForm()  # GET request form
    return render(request, 'base.html', {'form': form})


def list_items(request):
    list = Student.objects.all()
    return render(request, 'stud_list.html', {'lists': list})
