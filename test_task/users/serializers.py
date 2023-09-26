from rest_framework import serializers
from .models import Order, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Order
        fields = '__all__'
