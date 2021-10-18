from django.urls import path
from .views import (
    EmployeeProfileDetailView,
    EmployeeProfileListCreateView,
    TaskListCreateView,
    TaskDetailView,
)

urlpatterns = [
    path("all-profiles", EmployeeProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", EmployeeProfileDetailView.as_view(), name="profile"),
    path("all-tasks", TaskListCreateView.as_view(), name="all-tasks"),
    path("task/<int:pk>", TaskDetailView.as_view(), name="task")
]