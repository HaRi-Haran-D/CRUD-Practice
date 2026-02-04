from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm, LoginForm

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


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = LoginForm.cleaned_data['username']
            pwd = LoginForm.cleaned_data['password']
            try:
                user = User.objects.get(username=uname,password=pwd)
                request.session['user_id']=user.id
                return redirect('home')
            except User.DoesNotExist:
                return render(request, 'login.html', {'form':form, 'error':"Invalid Username or Password"})
    else:
        form = LoginForm()
    return render(request, 'form.html', {'form':form})


def logout(request):
    request.session.flush()
    return redirect('login')