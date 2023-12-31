from datetime import datetime, timedelta
from django.utils import timezone
import math
from django.contrib.auth.models import User, Group
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _



class Classroom(models.Model):
    name = models.CharField(max_length=255)
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'


class Student(models.Model):
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.ImageField(upload_to = 'images/', height_field=None, width_field=None, max_length=100, null=True, blank=True)
    phone_number=models.CharField(max_length=15, null=True, blank=True)
    parent_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'


# round time with 30 minutes for schedule
def round_dt(dt, delta):
    return datetime.min + math.floor((dt - datetime.min) / delta) * delta


delta = timedelta(minutes=30)
start_time = round_dt(datetime.now(), delta=delta)
end_time = round_dt(datetime.now(), delta) + timedelta(hours=2, minutes=30)


# start_time = now.strftime("%H:%M:%S")

def double_minutes(minute):
    if minute < 10:
        return '0' + str(minute)
    else:
        return minute


class Schedule(models.Model):
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # start_hour=models.DateTimeField(default=round_dt(datetime.now(), delta))
    # end_hour=models.DateTimeField(default=round_dt(datetime.now(), delta)+ timedelta(hours=2, minutes=30))
    start_hour = models.TimeField(default=start_time.time())
    end_hour = models.TimeField(default=end_time.time())
    created = models.DateField(auto_now_add=True)
    # presence_list= models.JSONField('Presence List',null=True,blank=True)

    weekDaysMapping = ("Monday", "Tuesday",
                       "Wednesday", "Thursday",
                       "Friday", "Saturday",
                       "Sunday")

    def get_week_day(self):
        return self.weekDaysMapping[self.created.weekday()]

    def get_students(self):
        return Student.objects.filter(classroom_id=self.classroom_id)

    def __str__(self) -> str:
        return "%s: %s:%s - %s:%s" % \
            (self.classroom_id.name, \
             self.start_hour.hour, \
             double_minutes(self.start_hour.minute), \
             self.end_hour.hour, \
             double_minutes(self.end_hour.minute))


class Present(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=True)
    notes = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{self.student}  {self.is_present}'

