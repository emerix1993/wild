from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    probation = models.BooleanField(default=False)
    position = models.CharField(max_length=255)


class Order(models.Model):
    task_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
