from django.forms import CharField, ModelForm, ModelChoiceField, PasswordInput
from .models import Student, Classroom, Schedule, Present
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django.forms.fields import EmailField
from django.core.exceptions import ValidationError  


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
    teacher_id = ModelChoiceField(queryset=User.objects.filter(groups__name='Teacher'))
    # created_by = ModelChoiceField(queryset=User.objects.filter(groups__name='Teacher'))


class ScheduleForm(ModelForm):
    class Meta:
        model= Schedule
        fields = ['start_hour', 'end_hour']


class PresenceForm(ModelForm):
    class Meta:
        model = Present
        fields = ['is_present', 'student']


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name','last_name', 'username','password1','password2'] 