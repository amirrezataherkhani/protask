# Generated by Django 4.1 on 2022-09-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0010_inviterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
