from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

class CreateStudent(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'app/form.html'


class StudentList(ListView):
    model = Student
    template_name = 'app/student_list.html'
    context_object_name = 'lists'


class StudentDetail(DetailView):
    model = Student
    template_name = 'app/detail.html'
    context_object_name = 'list'

class UpdateStudent(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'app/form.html'

class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy('app:home')
