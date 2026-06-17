from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Student
from .serializers import *
from .forms import StudentForm


# Create your views here.
class StudentView(APIView):

    def post(self, request):
        stud = StudentSerializer(data = request.data)
        if stud.is_valid():
            stud.save()
            return Response("Student Data Added")
        return Response(stud.errors)

    def get(self, request, id=None):
        if id==None:
            stud = Student.objects.all()
            serializer = StudentSerializer(stud, many=True)
            return Response(serializer.data)
        else:
            stud = Student.objects.get(id=id)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)

    def put(self, request, id):
        stud = Student.objects.get(id=id)
        serializer = StudentSerializer(stud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Updated")
        return Response(serializer.errors)

    def patch(self, request, id):
        stud = Student.objects.get(id=id)
        serializer = StudentSerializer(stud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Updated")
        return Response(serializer.errors)

    def delete(self, request, id):
        stud = Student.objects.get(id=id)
        stud.delete()
        return Response("Studdent Data Deleted")
















def student_list(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'home.html', {'form':form})


def home(request):
    list = Student.objects.all()
    return render(request, 'list.html', {'list':list})


def update_list(request, id):
    stud = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=stud)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'update.html', {'form':form})


def delete_list(request,id):
    form = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        form.delete()
        return redirect('list')
    return redirect('list')


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer