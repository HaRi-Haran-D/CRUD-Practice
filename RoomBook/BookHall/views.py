from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
class RoomBookView(generics.CreateAPIView):

    def perform_create(self, serializer):
        serializer.save()

    queryset = RoomBook.objects.all()
    serializer_class = RoomBookSerializer

    
        