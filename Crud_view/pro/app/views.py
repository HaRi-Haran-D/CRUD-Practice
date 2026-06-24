# from django.shortcuts import render
# from .models import Employee
# from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# from django.urls import reverse_lazy

# # Create your views here.
# def home(request):
#     return render(request, 'app/home.html')


# class CreateEmployee(CreateView):
#     model = Employee
#     fields = '__all__'
#     template_name = 'app/create.html'


# class ListEmployee(ListView):
#     model = Employee
#     template_name = 'app/list.html'
#     context_object_name = 'lists'


# class EmployeeDetail(DetailView):
#     model = Employee
#     template_name = 'app/detail.html'
#     context_object_name = 'list'


# class UpdateEmployee(UpdateView):
#     model = Employee
#     fields = '__all__'
#     template_name = 'app/create.html'
#     success_url = reverse_lazy('app:list')


# class DeleteEmployee(DeleteView):
#     model = Employee
#     success_url = reverse_lazy('app:list')














from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


class EmployeeView(APIView):

    def get(self, request, id=None):
        if id==None:
            employee = Employee.objects.all()
            serializer = EmployeeSerializer(employee, many=True)
            return Response(serializer.data)
        else:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)


    def post(self, request):
        employee = EmployeeSerializer(data=request.data)
        if employee.is_valid():
            employee.save()
            return Response("New Data Added")
        return Response(employee.errors)


    def put(self, request, id):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("New Data Added")
        return Response(serializer.errors)


    def patch(self,request,id):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("New Data Added")
        return Response(serializer.errors)


    def delete(self, request, id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response("Employee Deleted")



@api_view(["GET","POST"])
def create_post_data(request):

    if request.method == "GET":
        detail = Details.objects.all()
        serializer = DetailsSerializer(detail, many=True)
        return Response(serializer.data)


    elif request.method == "POST":
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("New Data Added")
        return Response(serializer.errors)



@api_view(["GET","PUT","PATCH","DELETE"])
def update_delete_data(request, id):
    detail = Details.objects.get(id=id)

    if request.method == 'GET':
        serializer = DetailsSerializer(detail)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = DetailsSerializer(detail, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Updated")
        return Response(serializer.errors)
    
    elif request.method == "PATCH":
        serializer = DetailsSerializer(detail, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Updated")
        return Response(serializer.errors)
    
    elif request.method == "DELETE":
        detail.delete()
        return Response("Data Deleted")
