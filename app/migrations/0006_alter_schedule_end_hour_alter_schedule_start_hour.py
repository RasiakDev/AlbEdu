# Generated by Django 4.2.6 on 2023-11-07 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_schedule_end_hour_alter_schedule_start_hour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_hour',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_hour',
            field=models.TimeField(default=datetime.time(9, 30)),
        ),
    ]