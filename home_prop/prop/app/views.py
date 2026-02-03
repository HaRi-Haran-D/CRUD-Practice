from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
            return redirect('home')
    else:
        form=UserForm()
    return render(request, 'register.html', {'form':form})


def list(request):
    list = User.objects.all()
    return render(request, 'list.html', {'list':list})

