from logging import getLogger
from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render
from app.forms import StudentForm
from ..models import Student
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def student_view(request):
    # shows to parents only their child
    def show_students(request):
        current_user = request.user
        users_groups = [group.name for group in current_user.groups.all()]
        if "Parent" in users_groups:
            return Student.objects.filter(parent_id=current_user.id)
        else:
            return Student.objects.all()

    object_list = show_students(request)
    context = {'object_list': object_list}
    return render(request, 'students/students_view.html', context=context)


class StudentProfile(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    template_name = 'students/student_profile.html'
    permission_required = "app.view_student"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)


LOGGER = getLogger()


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StudentForm
    template_name = 'students/create_student_form.html'
    success_url = reverse_lazy('student')
    permission_required = "app.create_student"

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
