from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student

# Create your views here.
def add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Form has be added")
        return redirect('app:add')
    return render(request, 'app/add.html', {'form':form})