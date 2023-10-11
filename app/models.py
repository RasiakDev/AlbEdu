from datetime import datetime, timedelta, timezone
import math
from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.



class Parent(models.Model):
    name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class Teacher(models.Model):
    name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'


class Classroom(models.Model):
    name=models.CharField(max_length=255)
    teacher_id=models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    created=models.DateTimeField(auto_now_add=True)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'


class Student(models.Model):
    name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    classroom_id=models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True)
    parent_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'


#round time with 30 minutes for schedule
def round_dt(dt, delta):
    return datetime.min + math.floor((dt - datetime.min) / delta) * delta
delta = timedelta(minutes=30)

def double_minutes(minute):
    if minute < 10:
        return '0' + str(minute)
    else:
        return minute
    
class Schedule(models.Model):
    classroom_id=models.ForeignKey(Classroom, on_delete=models.CASCADE)
    start_hour=models.DateTimeField(default=round_dt(datetime.now(), delta))
    end_hour=models.DateTimeField(default=round_dt(datetime.now(), delta)+ timedelta(hours=2, minutes=30))
    created=models.DateTimeField(auto_now_add=True)
    presence_list= models.JSONField('Presence List')

    def __str__(self) -> str:
        return "%s: %s %s:%s - %s:%s" % \
            (self.classroom_id.name, \
             self.start_hour.date(),\
            self.start_hour.hour, \
            double_minutes(self.start_hour.minute),\
            self.end_hour.hour, \
            double_minutes(self.end_hour.minute))