from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ProductModel
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request, 'app_folder/home.html')

def productlist(request):
    product = ProductModel.objects.all()
    return render(request, 'app_folder/product_list.html', {'product':product})

def createproduct(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        product = form.cleaned_data.get('product_name')
        messages.success(request, f"{product} has been added")
        return redirect('app_folder:home')
    return render(request, 'app_folder/create_product.html', {'form':form})