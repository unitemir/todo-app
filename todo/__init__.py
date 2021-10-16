from django.db.models import TextChoices


class TaskStatusChoice(TextChoices):
    NOT_STARTED = 'not_started', 'Не начато'
    IN_PROGRESS = 'in_progress', 'Выполняется'
    DONE = 'done', 'Выполнено'