from rest_framework.serializers import ModelSerializer
from .models import *

class StudentSerializer(ModelSerializer):
    class Mata:
        model=Student
        fields='__all__'

        
