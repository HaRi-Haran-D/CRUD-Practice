from django.shortcuts import render, redirect, get_object_or_404
from .models import Students
from .forms import StudentForms

# Create your views here.
def index(request):
    form = StudentForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app:index')
    return render(request, 'app/index.html', {'form':form})


def updateform(request,id):
    entry = Students.objects.get(id=id)
    form = StudentForms(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        return redirect('app:listitem')
    return render(request, 'app/update.html', {'form':form})


def listitem(request):
    list = Students.objects.all()
    return render(request, 'app/list.html', {'list':list})


def deleteitem(request, id):
    elem = get_object_or_404(Students, id=id)
    if request.method == "POST":
        elem.delete()
        return redirect('app:listitem')
    return redirect('app:listitem')