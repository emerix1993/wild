from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from test_task.users import view


router = DefaultRouter()
router.register(r'orders', view.OrderViewSet)
router.register(r'employees', view.EmployeeViewSet)

urlpatterns = [
    path('api/', include(router.urls))]
