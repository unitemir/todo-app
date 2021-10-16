from django.contrib import admin
from todo.models import Employee, Task


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'task_status', 'deadline')

    def has_change_permission(self, request, obj=None):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return True
        return False