# from django.shortcuts import render
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# from django.urls import reverse_lazy
# from .models import Student

# # Create your views here.
# def home(request):
#     return render(request, 'app/home.html')

# class CreateStudent(CreateView):
#     model = Student
#     fields = '__all__'
#     template_name = 'app/form.html'


# class StudentList(ListView):
#     model = Student
#     template_name = 'app/student_list.html'
#     context_object_name = 'lists'


# class StudentDetail(DetailView):
#     model = Student
#     template_name = 'app/detail.html'
#     context_object_name = 'list'

# class UpdateStudent(UpdateView):
#     model = Student
#     fields = '__all__'
#     template_name = 'app/form.html'

# class DeleteStudent(DeleteView):
#     model = Student
#     success_url = reverse_lazy('app:home')





















from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class StudentView(APIView):

    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response("New Student Added")
        return Response(student.errors)

    def get(self, request, id=None):
        if id==None:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        else:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Updated")
        return Response(serializer.errors)

    def patch(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Updated")
        return Response(serializer.errors)

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response("Student Deleted")

