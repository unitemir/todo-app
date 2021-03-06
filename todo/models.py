from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from todo import TaskStatusChoice


class Employee(AbstractUser):
    def __str__(self):
        return f'{self.username}'


class Task(models.Model):
    employee = models.ForeignKey(
                                 "Employee",
                                 on_delete=models.CASCADE,
                                 related_name='employee_task',
                                 verbose_name='Персонал'
    )
    title = models.CharField("Загаловок", max_length=255, null=False, blank=False)
    description = models.TextField("Описание", null=False, blank=False)
    task_status = models.CharField(
                                    "Статус",
                                    max_length=255,
                                    choices=TaskStatusChoice.choices,
                                    default=TaskStatusChoice.NOT_STARTED,
                                    null=False,
                                    blank=False,
    )
    deadline = models.DateTimeField("Дедлайн", db_index=True, default=timezone.now, null=False, blank=False)
