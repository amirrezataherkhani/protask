# Generated by Django 4.1 on 2022-09-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_room_request_string'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='joinrequest',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='joinrequest',
            name='status',
            field=models.CharField(choices=[('p', 'Pending'), ('a', 'Accepted'), ('r', 'Rejected')], default='p', max_length=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='request_string',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
