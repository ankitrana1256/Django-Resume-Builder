# Generated by Django 3.1.4 on 2022-04-22 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20220422_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectorjob',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 22, 15, 21, 13, 380731)),
        ),
        migrations.AlterField(
            model_name='projectorjob',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 22, 15, 21, 13, 380731)),
        ),
    ]
