# from django.shortcuts import render, redirect
# from .models import User
# from .forms import UserForm, LoginForm

# # Create your views here.
# def home(request):
#     user_id = request.session.get('user_id')
#     user = None
#     if user_id:
#         user = User.objects.get(id=user_id)

#     return render(request, 'base.html', {'user': user})


# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = UserForm()
#             return redirect('home')
#     else:
#         form = UserForm()
#     return render(request, 'register.html', {'form':form})


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             uname = form.cleaned_data['username']
#             pwd = form.cleaned_data['password']
#             try:
#                 user = User.objects.get(username=uname, password=pwd)
#                 request.session['user_id'] = user.id
#                 return redirect('home')
#             except User.DoesNotExist:
#                 return render(request, 'login.html', {
#                     'form': form,
#                     'error': "Invalid Username or Password"
#                 })
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})


# def logout(request):
#     request.session.flush()
#     return redirect('login')

















from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import permissions
from .models import *
from .serializers import *


class StudentView(APIView):

    def get(self, request, id=None):
        if id == None:
            student_data = Student.objects.all()
            serializer = StudentSerializer(student_data, many=True)
            return Response(serializer.data)
        else:
            student_data = Student.objects.get(id=id)
            serializer = StudentSerializer(student_data)
            return Response(serializer.data)


    def post(self, request):
        student_data = StudentSerializer(data=request.data)
        if student_data.is_valid():
            student_data.save()
            return Response("Student Data Added")
        return Response(student_data.errors)



class DataBaseView(ModelViewSet):
    queryset = DataBase.objects.all()
    serializer_class = DataBaseSerializer


class DatabaseGenericView(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(description="Manga")
    
    queryset = DataBase.objects.all()
    serializer_class = DataBaseSerializer



class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset=self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)