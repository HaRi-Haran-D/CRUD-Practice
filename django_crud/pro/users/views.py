from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def registerform(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Registered")
        return redirect('home:index')
    return render(request, 'users/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('users:login')
