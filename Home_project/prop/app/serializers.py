from rest_framework.serializers import ModelSerializer
from .models import *


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DataBaseSerializer(ModelSerializer):
    class Meta:
        model = DataBase
        fields = ['title', 'description']
