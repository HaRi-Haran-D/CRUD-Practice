from rest_framework.serializers import ModelSerializer
from .models import *

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class StudentTaskSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'


class TaskStudSerializer(ModelSerializer):
    student_ref = StudentSerializer()
    class Meta:
        model = Task
        fields = '__all__'
