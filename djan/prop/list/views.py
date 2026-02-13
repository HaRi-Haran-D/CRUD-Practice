from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import List
from .forms import ListForm

# Create your views here.
def post(request):
    lists = List.objects.all().order_by('-date')
    return render(request, 'list/list.html', {'lists':lists})


def post_list(request, slug):
    post = List.objects.get(slug=slug)
    return render(request, 'list/post_list.html', {'post':post})


@login_required(login_url ='users:login')
def posts_new(request):
    if request.method == 'POST':
        form = ListForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save()
            newpost.author = request.user
            newpost.save()
            return redirect('list:new-post')
    else:
        form = ListForm()
    return render(request, 'list/post_new.html', {'form':form})
