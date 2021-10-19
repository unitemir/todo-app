from django.urls import path
from .views import (
    EmployeeProfileDetailView,
    EmployeeProfileListCreateView,
    TaskListCreateView,
    TaskDetailView,
    TaskCreateView,
)

urlpatterns = [
    path("all-profiles", EmployeeProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", EmployeeProfileDetailView.as_view(), name="profile"),
    path("all-tasks", TaskListCreateView.as_view(), name="all-tasks"),
    path("task/create", TaskCreateView.as_view(), name="create-task"),
    path("task/<int:pk>", TaskDetailView.as_view(), name="task"),
]