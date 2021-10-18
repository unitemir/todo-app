from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Task
from .permissions import IsOwnerProfileOrReadOnly, IsOwnerTaskOrReadOnly
from .serializers import EmployeeSerializer, TaskSerializer


class EmployeeProfileListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        employee = self.request.user
        serializer.save(user=employee)


class EmployeeProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerTaskOrReadOnly, IsAuthenticated]
