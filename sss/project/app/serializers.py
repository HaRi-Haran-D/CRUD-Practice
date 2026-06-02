from .models import Stud
from rest_framework.serializers import ModelSerializer


class StudSerializer(ModelSerializer):
    class Meta:
        model = Stud
        fields = '__all__'