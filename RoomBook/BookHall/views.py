from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *


# Create your views here.
class RoomBookView(APIView):

    def get(self, request, id=None):
        if id==None:
            bookings = RoomBook.objects.all()
            serializer = RoomBookSerializer(bookings, many=True)
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        else:
            bookings = RoomBook.objects.get(id=id)
            serializer = RoomBookSerializer(bookings)
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )


    def post(self, request):
        book = RoomBookSerializer(data=request.data)
        if book.is_valid():
            date = book.save()
            return Response(
                {
                "success":True,
                "message":(
                    f"Room Booked on"
                    f" Start Time: {date.start_time.strftime("%H:%M")}"
                    f" End Time: {date.end_time.strftime("%H:%M")}"
                )
                },
                status = status.HTTP_200_OK
            )
        return Response(
            {
                "success":False,
                "message":book.errors
            },
            status = status.HTTP_400_BAD_REQUEST
        )



