# Generated by Django 4.1 on 2022-10-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_alter_task_status_phase_task_phase'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
