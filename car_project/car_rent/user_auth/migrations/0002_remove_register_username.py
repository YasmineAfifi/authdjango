# Generated by Django 4.2.7 on 2023-11-29 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
    ]
