from django.forms import CharField, ModelForm, Form, ModelChoiceField
from django.views.generic.edit import FormView
from .models import Parent, Student, Classroom
from django.urls import reverse_lazy

class ParendForm(ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"

# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = "__all__"
    
#     def clean(self):
#         result = super().clean()
        
#         return result

#     # def clean(self):
#     #     result = super().clean()
#     #     return result


# class StudentForm(Form):

#   name = CharField(max_length=128)
#   last_name = CharField(max_length=128)
#   classroom_id = ModelChoiceField(queryset=Classroom.objects.all())
#   parent_id = ModelChoiceField(Parent.objects.all())

 