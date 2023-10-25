# Generated by Django 4.2.5 on 2023-10-25 17:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_schedule_presence_list_student_presence_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_hour',
            field=models.TimeField(default=datetime.time(22, 0)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_hour',
            field=models.TimeField(default=datetime.time(19, 30)),
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence', models.BooleanField(default=False)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.schedule')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.classroom')),
            ],
        ),
    ]
