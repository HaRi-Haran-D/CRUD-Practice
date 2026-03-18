from django.shortcuts import render, redirect, get_object_or_404
from .forms import ModelForming
from .models import ModelForms

# Create your views here.
def home(request):
    form = ModelForming(request.POST or None)
    
    if form.is_valid():
        obj = form.save(commit=False)

        if not obj.image:
            obj.image = "https://static.thenounproject.com/png/4595376-200.png"

        obj.save()
        return redirect('home')

    return render(request, 'app/home.html', {'form': form})
    # form =  ModelForming(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('home')
    # return render(request, 'app/home.html', {'form':form})

def update(request):
    pass

def listitem(request):
    list = ModelForms.objects.all()
    return render(request, 'app/list.html', {'list':list})