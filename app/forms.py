from typing import Any
from django.forms import CharField, ModelForm, ModelChoiceField, TimeField, ChoiceField, Select, Form, BooleanField
from .models import Parent, Student, Classroom, Teacher, Schedule, Present
from django.contrib.auth.models import User

class ParendForm(ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields='__all__'    
    
    name = CharField(max_length=128)
    last_name = CharField(max_length=128)
    parent_id = ModelChoiceField(queryset= User.objects.filter(groups__name='Parent'))
    classroom_id = ModelChoiceField(queryset=Classroom.objects.all())

    def clean_name(self):
        initial = self.cleaned_data['name']
        name = initial.capitalize()
        return name
    def clean_last_name(self):
        initial = self.cleaned_data['last_name']
        last_name = initial.capitalize()
        return last_name
    
class ClassroomForm(ModelForm):
    
    class Meta:
        model = Classroom
        fields = '__all__'

    name = CharField(max_length=255)
    teacher_id = ModelChoiceField(queryset=Teacher.objects.all())
    # created_by = ModelChoiceField(queryset=User.objects.filter(groups__name='Teacher'))


class ScheduleForm(ModelForm):
    class Meta:
        model= Schedule
        fields = ['start_hour', 'end_hour']


class PresenceForm(ModelForm):
    class Meta:
        model = Present
        fields = ['presence']