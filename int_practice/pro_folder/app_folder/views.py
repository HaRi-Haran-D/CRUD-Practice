from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ProductModel
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request, 'app_folder/home.html')

def productlist(request):
    products = ProductModel.objects.all()
    return render(request, 'app_folder/product_list.html', {'products':products})

def createproduct(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        product = form.cleaned_data.get('product_name')
        messages.success(request, f"{product} has been added")
        return redirect('app_folder:home')
    return render(request, 'app_folder/create_product.html', {'form':form})

def updateproduct(request, id):
    product = get_object_or_404(ProductModel,id=id)
    form = ProductForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
        return redirect('app_folder:product_list')
    return render(request, 'app_folder/update_product.html', {'form':form})

def deleteproduct(request,id):
    product = get_object_or_404(ProductModel,id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('app_folder:product_list')
    return render(request, 'app_folder/delete_product.html')