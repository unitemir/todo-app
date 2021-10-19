# Generated by Django 3.2.8 on 2021-10-18 11:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, verbose_name='Дедлайн'),
        ),
    ]