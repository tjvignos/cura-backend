# Generated by Django 4.0 on 2024-04-05 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0004_alter_checkin_user'),
        ('circle', '0005_alter_circle_users'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
