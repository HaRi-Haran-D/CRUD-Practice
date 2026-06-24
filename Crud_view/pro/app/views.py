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


    