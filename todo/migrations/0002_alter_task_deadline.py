# Generated by Django 3.2.8 on 2021-10-16 04:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, db_index=True, default=django.utils.timezone.now, verbose_name='Дедлайн'),
        ),
    ]
