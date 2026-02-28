from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

# Create your views here.
class StudentList(CreateView):
    model = Student
    template_name = 'form.html'
    