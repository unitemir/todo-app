from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeeProfileDetailView, EmployeeProfileListCreateView, TaskListCreateView

urlpatterns = [
    path("all-profiles",EmployeeProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>",EmployeeProfileDetailView.as_view(),name="profile"),
    path("all-tasks", TaskListCreateView.as_view(), name="tasks"),
    # path("task/<int:pk>")
]