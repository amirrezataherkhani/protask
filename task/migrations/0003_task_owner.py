# Generated by Django 4.1 on 2022-09-05 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_remove_room_tasks'),
        ('task', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_tasks', to='room.room'),
        ),
    ]
