# Generated by Django 4.2.5 on 2023-10-02 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_schedule_end_hour_alter_schedule_start_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 2, 17, 45)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 2, 15, 15)),
        ),
    ]
