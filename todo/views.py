from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import EmployeeSerializer

class EmployeeProfileListCreateView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        employee=self.request.user
        serializer.save(user=employee)


class EmployeeProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]