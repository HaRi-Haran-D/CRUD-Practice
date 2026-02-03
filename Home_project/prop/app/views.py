from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm, LoginForm

# Create your views here.
def home(request):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        user = User.objects.get(id=user_id)

    return render(request, 'base.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            try:
                user = User.objects.get(username=uname, password=pwd)
                request.session['user_id'] = user.id
                return redirect('home')
            except User.DoesNotExist:
                return render(request, 'login.html', {
                    'form': form,
                    'error': "Invalid Username or Password"
                })
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    request.session.flush()
    return redirect('login')
