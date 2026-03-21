from django.shortcuts import render
from .models import Employee
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'app/home.html')


class CreateEmployee(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'app/create.html'


class ListEmployee(ListView):
    model = Employee
    template_name = 'app/list.html'
    context_object_name = 'lists'


class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'app/detail.html'
    context_object_name = 'list'


class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'app/create.html'
    success_url = reverse_lazy('app:list')


class DeleteEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('app:list')