from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form=StudentForm()
    else:
        form = StudentForm()  # GET request form

    return render(request, 'base.html', {'form': form})
