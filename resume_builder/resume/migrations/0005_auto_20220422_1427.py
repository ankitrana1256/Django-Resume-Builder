# Generated by Django 3.1.4 on 2022-04-22 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20220422_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectorjob',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projectorjob',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 22, 14, 27, 46, 917165)),
        ),
        migrations.AlterField(
            model_name='projectorjob',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 22, 14, 27, 46, 917165)),
        ),
    ]
