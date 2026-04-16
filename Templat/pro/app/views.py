from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm

# Create your views here.
# @login_required
# def home(request):
#     items = Item.objects.all()
#     return render(request, 'app/index.html', {'items':items})

class IndexClassView(ListView):
    model = Item
    template_name = 'app/index.html'
    context_object_name = 'items'


# def detail(request, id):
#     items = Item.objects.get(id=id)
#     return render(request, 'app/details.html', {'items':items})


class FoodDetailView(DetailView):
    model = Item
    template_name = 'app/details.html'
    context_object_name = 'items'

# def create(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('app:home')
#     return render(request, 'app/form.html', {'form':form})


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'price', 'descri', 'image']

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    

# def update(request, id):
#     item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('app:home')
#     return render(request, 'app/form.html', {'form':form})


class ItemUpdateView(UpdateView):
    model = Item
    fields = '__all__'
    template_name = 'app/item_update_form.html'
    
    def get_queryset(self):
        return Item.objects.filter(user_name = self.request.user)


def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('app:home')
    return render(request, 'app/delete.html')


# class ItemDeleteView(DeleteView):
#     model = Item
#     success_url = reverse_lazy('app:home')


# def get_objects(request):
#     for item in Item.objects.all():
#         print(item.name)

# def get_objects_optimized(request):
#     items = Item.objects.only('name')
#     for item in items:
#         print(item.name)