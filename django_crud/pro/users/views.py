from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def registerform(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home:index')
    return render(request, 'users/register.html', {'form':form})


