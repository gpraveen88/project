# Generated by Django 3.2.16 on 2023-01-18 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0008_auto_20230118_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_call',
            name='ChooseDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 11, 48, 53, 965476)),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 11, 48, 53, 965476)),
        ),
    ]
