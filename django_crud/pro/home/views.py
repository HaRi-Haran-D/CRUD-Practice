from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.
@login_required
def index(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.name = request.user 
        form.save()
        messages.success(request,"Your post has been Successfully posted!")
        return redirect('home:index')
    return render(request, 'home/index.html', {'form':form})


def posts(request):
    post = Post.objects.all()
    return render(request, 'home/posts.html',{'posts':post})