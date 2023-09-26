from django.shortcuts import render

from rest_framework import viewsets
from .models import Order, Employee
from .serializers import OrderSerializer, EmployeeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
