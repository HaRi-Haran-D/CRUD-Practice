from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Stud
from .serializers import StudSerializer

# Create your views here.
# def home(request):    
#     form = StudForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     return render(request, 'app\home.html', {'form':form})

class StudAPI(APIView):
    
    def get(self, request):
        student = Stud.objects.all()
        list = StudSerializer(student, many=True)
        return Response(list.data)
    
    def post(self, request):
        student = StudSerializer(data = request.data)
        if student.is_valid():
            student.save()
            return Response("New Student Added")
        return Response(student.errors)

class StudAPIByID(APIView):
    
    def get(self, request, id):
        student = Stud.objects.get(id=id)
        serializer = StudSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, id):
        student = Stud.objects.get(id=id)
        serializer = StudSerializer(student, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student has Been Updated")
        return Response(serializer.errors)
    
    def patch(self, request, id):
        student = Stud.objects.get(id=id)
        serializer = StudSerializer(student, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student has Been Updated")
        return Response(serializer.errors)