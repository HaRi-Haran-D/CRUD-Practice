# from django.shortcuts import render, redirect
# from django.shortcuts import get_object_or_404
# from django.core.paginator import Paginator
# from .forms import StudentForm
# from .models import Student


# # Create your views here.
# def home(request):
#     # if request.method == 'POST':
#     #     form = StudentForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         form = StudentForm()
#     #         return redirect('home')
#     # else:
#     #     form = StudentForm()
#     # return render(request, 'base.html', {'form':form})
#     form = StudentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('list')
#     return render(request, 'base.html', {'form':form})


# def list(request):
#     list = Student.objects.all()
#     paginator = Paginator(list,1)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'list.html', {'page_obj':page_obj})


# def update(request,item_id):
#     # item = Student.objects.get(id=item_id)
#     # form = StudentForm(instance=item)
#     # if request.method == 'POST':
#     #     form = StudentForm(request.POST, instance=item)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('list')
#     # return render(request, 'update.html', {'form':form})
#     item = Student.objects.get(id=item_id)
#     form = StudentForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('list')
#     return render(request, 'base.html', {'form':form})


# def delete(request, item_id):
#     std = get_object_or_404(Student, id=item_id)
#     if request.method == 'POST':
#         std.delete()
#         return redirect('list')
#     return redirect('list')










from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import *
from .serializers import *


class StudentAPIView(APIView):

    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response("Student Added")
        return Response(student.errors)


    def get(self, request, id=None):
        if id == None:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        else:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)


    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Updated")
        return Response(serializer.errors)


    def patch(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Updated")
        return Response(serializer.errors)


    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response("Student Deleted")
