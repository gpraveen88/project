# Generated by Django 3.2.16 on 2023-01-12 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0003_auto_20230112_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='InitialInvestmentAmount',
        ),
    ]