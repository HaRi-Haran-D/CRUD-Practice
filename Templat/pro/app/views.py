from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm

# Create your views here.
@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'app/index.html', {'items':items})

# class IndexClassView():
     


def detail(request, id):
    items = Item.objects.get(id=id)
    return render(request, 'app/details.html', {'items':items})


def create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app:home')
    return render(request, 'app/form.html', {'form':form})


def update(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('app:home')
    return render(request, 'app/form.html', {'form':form})


def delete(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('app:home')
    return render(request, 'app/delete.html')