# Generated by Django 4.2.5 on 2023-10-25 18:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_schedule_end_hour_alter_schedule_start_hour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='present',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.student'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_hour',
            field=models.TimeField(default=datetime.time(22, 30)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_hour',
            field=models.TimeField(default=datetime.time(20, 0)),
        ),
    ]