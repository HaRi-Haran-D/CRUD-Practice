from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User

# Create your views here.

class UserView(APIView):

    def post(self, request):
        new_user = User(username = request.data['username'], is_superuser=request.data['is_superuser'])
        new_user.set_password(request.data['password'])
        new_user.save()
        return Response("New user added")
    
    