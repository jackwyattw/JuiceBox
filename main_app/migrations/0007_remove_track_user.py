# Generated by Django 4.1.2 on 2022-10-16 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_track_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='user',
        ),
    ]