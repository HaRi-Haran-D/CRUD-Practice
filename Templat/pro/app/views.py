from django.shortcuts import render
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'app/index.html', {'items':items})

def detail(request, id):
    items = Item.objects.get(id=id)
    return render(request, 'app/details.html', {'items':items})