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

# def update_list(request,item_id):
#     items = Student.objects.get(id=item_id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=items)
#         form.save()
#         return redirect('list_items')
#     return render(request,'update_list.html', {'form':form})

def update_list(request, item_id):
    items = Student.objects.get(id=item_id)
    form = StudentForm(instance=items)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    return render(request, 'update_list.html', {'form': form})

        