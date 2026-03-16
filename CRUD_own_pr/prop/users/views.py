from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
def login(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'users/login.html', {'form':form})