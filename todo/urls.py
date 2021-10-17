from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeeProfileDetailView, EmployeeProfileListCreateView

urlpatterns = [
    path("all-profiles",EmployeeProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>",EmployeeProfileDetailView.as_view(),name="profile"),
]