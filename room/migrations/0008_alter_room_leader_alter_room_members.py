# Generated by Django 4.1 on 2022-09-07 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0007_alter_joinrequest_options_alter_joinrequest_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms_own', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]