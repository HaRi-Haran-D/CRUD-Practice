from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import StudentForm
from .models import Student


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'base.html', {'form':form})


def list(request):
    list = Student.objects.all()
    return render(request, 'list.html', {'list':list})


def update(request,item_id):
    item = Student.objects.get(id=item_id)
    form = StudentForm(instance=item)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'update.html', {'form':form})


def delete(request, item_id):
    std = get_object_or_404(Student, id=item_id)
    if request.method == 'POST':
        std.delete()
        return redirect('list')
    return redirect('list')
