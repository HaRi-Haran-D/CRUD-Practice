from rest_framework.serializers import ModelSerializer
from .models import *


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'