from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
import datetime
from pytz import utc
from choco.celery import app
from todo import TaskStatusChoice
from todo.models import Task


@app.task()
def check_for_tasks():
    tasks = Task.objects.filter(task_status=[TaskStatusChoice.NOT_STARTED, TaskStatusChoice.IN_PROGRESS])
    hour_before_dl = datetime.datetime.utcnow().replace(
                                                        tzinfo=utc,
                                                        second=00,
                                                        microsecond=00) - datetime.timedelta(0, 3600)
    for task in tasks:
        if task.deadline == hour_before_dl:
            send_mail('Task Reminder',
                      f'the task {task.title} will close in an hour',
                      '',
                      [task.employee.email]
                      )
    return None
