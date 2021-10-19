from celery import Celery
from celery.schedules import crontab

app = Celery('core', include=['todo.tasks'])
app.config_from_object('choco.celeryconfig')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_for_tasks': {
        'task': 'todo.tasks.check_for_tasks',
        'schedule': crontab(minute=1),
    }
}

app.conf.timezone = "Asia/Almaty"
