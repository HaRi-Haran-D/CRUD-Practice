from django.shortcuts import render
from .models import List

# Create your views here.
def post(request):
    lists = List.objects.all().order_by('-date')
    return render(request, 'list/list.html', {'lists':lists})

def post_list(request, slug):
    post = List.objects.get(slug=slug)
    return render(request, 'list/post_list.html', {'post':post})