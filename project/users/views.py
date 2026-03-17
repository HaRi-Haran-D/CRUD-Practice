from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

# Create your views here.
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'users/register.html', {'form':form})