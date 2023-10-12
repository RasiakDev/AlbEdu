# Generated by Django 4.2.5 on 2023-10-12 11:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_schedule_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='presence_list',
            field=models.JSONField(blank=True, null=True, verbose_name='Presence List'),
        ),
    ]
