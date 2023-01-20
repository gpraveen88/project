# Generated by Django 3.2.16 on 2023-01-18 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0009_auto_20230118_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_call',
            name='Mobileno',
        ),
        migrations.AddField(
            model_name='request_call',
            name='MobileNo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request_call',
            name='ChooseDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 12, 52, 19, 789320)),
        ),
    ]