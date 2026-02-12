from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import List

# Create your views here.
def post(request):
    lists = List.objects.all().order_by('-date')
    return render(request, 'list/list.html', {'lists':lists})

def post_list(request, slug):
    post = List.objects.get(slug=slug)
    return render(request, 'list/post_list.html', {'post':post})


@login_required(login_url ='users:login')
def posts_new(request):
    return render(request, 'list/post_new.html')