# Generated by Django 4.1.1 on 2022-11-09 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_prioryty_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-04-22'),
            preserve_default=False,
        ),
    ]