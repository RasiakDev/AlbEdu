# from django.shortcuts import render
# from rest_framework import viewsets
from typing import Any
from logging import getLogger
from django.urls import reverse_lazy
from ..models import Parent, Student
# from ..forms import StudentForm
# from .serializers import ParentSerializer
from django.views.generic import TemplateView, DetailView, DeleteView, CreateView, FormView, ListView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import (
  LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.auth.models import User

# class ParentView(viewsets.ModelViewSet):
#     serializer_class = ParentSerializer
#     queryset = Parent.objects.all()

class SubmittableLoginView(LoginView):
  template_name = 'registration/login.html'

class IndexView(TemplateView):
    template_name = "base.html"
    extra_context = {'parents': Parent.objects.all(), 'students': Student.objects.all()}

class ParentView(DetailView):    
    template_name="parent.html"
    model = Parent

class StudentView(LoginRequiredMixin, ListView):
    template_name = 'student_profile.html'
    queryset = Student.objects.all()

class ParentDeleteView(DeleteView):
    template_name='registration/parent_confirm_delete.html'
    model = Parent
    success_url = reverse_lazy('index')
  
class StudentCreateView(PermissionRequiredMixin,CreateView):
    model = Student
    fields = '__all__'
    template_name = 'registration/create_student_form.html'
    success_url = reverse_lazy('student')
    permission_required = "app.create_student"

class StudentDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'registration/form_confirm_delete.html'
    model = Student
    success_url = reverse_lazy('student')
    permission_required='app.delete_student'
    
class StudentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Student
    template_name = 'registration/create_student_form.html'
    fields = '__all__'
    success_url= reverse_lazy('student')
    permission_required='app.change_student'