from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import PostForm
from .models import Post, Profile
from .serializers import *

# Create your views here.

class PostView(APIView):

    def post(self, request):
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response("Post has been Added")
        return Response(post.errors)
    
    def get(self, request):
        stud = Post.objects.all()
        serializer = PostSerializer(stud, many=True)
        return Response(serializer.data)

    










def create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.name = request.user 
        form.save()
        messages.success(request,"Your post has been Successfully posted!")
        return redirect('home:index')
    return render(request, 'home/create.html', {'form':form})


@login_required
def index(request):
    post = Post.objects.all()
    return render(request, 'home/index.html',{'posts':post})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    post = Post.objects.filter(name=user)
    return render(request, 'home/profile.html', {'posts':post})
    

def userprofile(request, username):
    user = get_object_or_404(User, username=username)
    post = Post.objects.filter(name=user)
    profile = Profile.objects.get(user=user)
    return render(request, 'home/userprofile.html', {'posts':post})