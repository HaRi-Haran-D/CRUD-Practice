from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home:index')
    return render(request, 'home/index.html', {'form':form})


def posts(request):
    post = Post.objects.all()
    return render(request, 'home/posts.html',{'posts':post})