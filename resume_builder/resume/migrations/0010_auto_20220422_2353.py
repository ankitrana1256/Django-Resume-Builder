# Generated by Django 3.1.4 on 2022-04-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20220422_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areaofinterest',
            name='person',
        ),
        migrations.RemoveField(
            model_name='projectorjob',
            name='person',
        ),
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Academics',
        ),
        migrations.DeleteModel(
            name='AreaOfInterest',
        ),
        migrations.DeleteModel(
            name='ProjectOrJob',
        ),
    ]
