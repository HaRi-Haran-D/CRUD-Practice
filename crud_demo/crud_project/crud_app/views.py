from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'home.html', {'form':form})


def student_list(request):
    list = Student.objects.all()
    return render(request, 'list.html', {'list':list})


def update_list(request, id):
    stud = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=stud)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'update.html', {'form':form})


def delete_list(request,id):
    form = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        form.delete()
        return redirect('list')
    return redirect('list')