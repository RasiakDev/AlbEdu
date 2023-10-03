# Generated by Django 4.2.5 on 2023-10-03 12:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_schedule_end_hour_alter_schedule_start_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='presentce',
            field=models.ManyToManyField(to='app.student'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='student',
            field=models.CharField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 17, 0)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_hour',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 14, 30)),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.classroom'),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.parent'),
        ),
    ]
