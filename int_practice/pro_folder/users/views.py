from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import User

# Create your views here.

class UserView(APIView):

    def post(self, request):
        new_user = User(username = request.data['username'], is_superuser=request.data['is_superuser'])
        new_user.set_password(request.data['password'])
        new_user.save()
        return Response("New user added")
    

class UserLoginView(APIView):

    def post(self, request):
        user_verification = authenticate(username=request.data['username'], password=request.data['password'])
        if user_verification == None:
            return Response("Invalid Username or Password")
        else:
            print(user_verification.username)
            return Response("Login")
