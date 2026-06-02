from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company
from .forms import CompanyForm
from .serializers import CompanySerializer

# Create your views here.
class CompanyAPI(APIView):
    def get(self, request):
        emp = Company.objects.all()
        company = CompanySerializer(emp, many=True)
        return Response(company.data)

    def post(self, request):
        emp = CompanySerializer(data=request.data)
        if emp.is_valid():
            emp.save()
            return Response("Employee has been added")
        return Response(emp.errors)


class CompanyAPIByID(APIView):

    def get(self, request, id):
        emp = get_object_or_404(Company,id=id)
        serializer = CompanySerializer(emp)
        return Response(serializer.data)
    
    def put(self, request, id):
        emp = Company.objects.get(id=id)
        serializer = CompanySerializer(emp, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Employee Data has been Updated")
        return Response(serializer.errors)

    def patch(self, request, id):
        emp = Company.objects.get(id=id)
        serializer = CompanySerializer(emp, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Employee Data has been Updated")
        return Response(serializer.errors)
    
    def delete(self, request, id):
        emp=Company.objects.get(id=id)
        emp.delete()
        return Response("Employee Has been Deleted")







def home(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=CompanyForm()
        messages.success(request, "Record added successfully.")
        return redirect('home')
    return render(request, 'index.html', {'form': form})


def emp_list(request):
    list = Company.objects.all()
    return render(request, 'emp_list.html', {'list':list})


def update_list(request, item_id):
    item = Company.objects.get(id=item_id)
    form = CompanyForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'emp_update.html', {'form': form})


def delete_list(request, item_id):
    emp = get_object_or_404(Company, id=item_id)
    if request.method == "POST":
        emp.delete()
        return redirect("list")
    return redirect("list")

