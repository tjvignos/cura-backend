# Generated by Django 4.0 on 2024-04-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('circle', '0003_alter_circle_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='users',
            field=models.ManyToManyField(related_name='circles', to='user.User'),
        ),
    ]