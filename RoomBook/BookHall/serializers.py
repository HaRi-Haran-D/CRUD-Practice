from rest_framework.serializers import ModelSerializer
from .models import RoomBook


class RoomBookSerializer(ModelSerializer):
    class Meta:
        model = RoomBook
        fields = ['booking_date', 'start_time', 'end_time']
