from django.urls import reverse_lazy
from ..models import Parent, Student
from django.views.generic import TemplateView, DetailView, DeleteView, CreateView, FormView, ListView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import (
  LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.auth.models import User

class SubmittableLoginView(LoginView):
  template_name = 'registration/login.html'

class IndexView(TemplateView):
    template_name = "base.html"
    extra_context = {'parents': Parent.objects.all(), 'students': Student.objects.all()}

class ParentView(DetailView):    
    template_name="parent.html"
    model = Parent

class ParentDeleteView(DeleteView):
    template_name='registration/parent_confirm_delete.html'
    model = Parent
    success_url = reverse_lazy('index')
  

