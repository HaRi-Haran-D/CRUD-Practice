from django.shortcuts import render, redirect, get_object_or_404
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


def listdata(request):
    lists = Student.objects.all()
    return render(request, 'app/list.html', {'lists':lists})


def updatedata(request, id):
    value = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=value)
    if form.is_valid():
        form.save()
        messages.success(request, "Form has been Updated Successfully")
        return redirect('app:lists')
    return render(request, 'app/add.html', {'form':form})


def deletedata(request, id):
    data = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('app:lists')
    return redirect('app:lists')