from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .forms import StudentForm
from .models import Student
from .serializers import *

# Create your views here.
def add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Form has be added")
        return redirect('app:add')
    return render(request, 'app/add.html', {'form':form})


def listdata(request):
    lists = Student.objects.all()
    return render(request, 'app/list.html', {'lists':lists})


def updatedata(request, id):
    value = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=value)
    if form.is_valid():
        form.save()
        messages.success(request, "Form has been Updated Successfully")
        return redirect('app:lists')
    return render(request, 'app/add.html', {'form':form})


def deletedata(request, id):
    data = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('app:lists')
    return redirect('app:lists')



class StudentView(APIView):

    def get(self, request, id=None):
        if id == None:
            student = Student.objects.all()
            serializer = StudentTaskSerializer(student, many=True)
            return Response(serializer.data)
        else:
            student = Student.objects.get(id=id)
            serializer = StudentTaskSerializer(student)
            return Response(serializer.data)

    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response("Student Added")
        return Response(student.errors)

    def patch(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("StudentUpdated")
        else:
            return Response(serializer.errors)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("StudentUpdated")
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response("Student Deleted")


class StudentTaskView(APIView):

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)



class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
