from rest_framework import serializers
from .models import Item, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ItemSerializer(serializers.ModelSerializer):
    user_name = UserSerializer(read_only = True)
    class Meta:
        model = Item
        fields = ["id", "user_name", "name", "descri", "price", "image"]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than Zero")
        return value

    def validate(self, data):
        if data['name'].lower() == data['descri'].lower():
            raise serializers.ValidationError("Item name and Descriptiion cannot be the same")
        return data

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = ["id", "user", "created_at", "items"]