from logging import getLogger
from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render
from app.forms import StudentForm
from ..models import Classroom, Student, Present, Schedule
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.template.defaulttags import register



@login_required(redirect_field_name='login')
@permission_required("app.view_student")
def student_view(request):
    # shows to parents only their child
    def show_students(request):
        current_user = request.user
        users_groups = [group.name for group in current_user.groups.all()]
        if "Parent" in users_groups:
            return Student.objects.filter(parent_id=current_user.id)
        else:
            return Student.objects.all()
        
    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)
    
    total_presences = Present.objects.all()
    object_list = show_students(request)
    presences_and_absences = {}
    students_classroom = {}
    
    for student in object_list:
        presences_and_absences[student] = [len(total_presences.filter(student=student, is_present=True)),len(total_presences.filter(student=student, is_present=False))]
        students_classroom[student] = Classroom.objects.get(student=student).name

    print(students_classroom)
    print(presences_and_absences)
    context = {'object_list': object_list, 'presences_and_absences' : presences_and_absences, 'students_classroom' : students_classroom}
    return render(request, 'students/students_view.html', context=context)


class StudentProfile(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    template_name = 'students/student_profile.html'
    permission_required = "app.view_student"    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(id=self.kwargs['pk'])
        presences = Present.objects.filter(student=student)
        presence_and_schedules = {}
        for presence in presences:
            presence_and_schedules[presence] = Schedule.objects.get(id= presence.schedule.id)

        parent = User.objects.get(id=student.parent_id.id)
        context['parent'] = parent
        context['presence_and_schedules'] = presence_and_schedules
        absences = [presence for presence in presences if presence.is_present == False]
        context['absences'] = absences
        presence_count = len(presences) - len(absences)
        context['presences'] = presence_count
        
        return context


LOGGER = getLogger()


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StudentForm
    template_name = 'students/create_student_form.html'
    success_url = reverse_lazy('student')
    permission_required = "app.add_student"

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'form_confirm_delete.html'
    model = Student
    success_url = reverse_lazy('student')
    permission_required = 'app.delete_student'


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    template_name = 'students/create_student_form.html'
    fields = '__all__'
    success_url = reverse_lazy('student')
    permission_required = 'app.change_student'
