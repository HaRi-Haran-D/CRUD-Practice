from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.

class UserView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


