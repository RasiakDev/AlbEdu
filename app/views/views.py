from ..models import Student
from django.views.generic import TemplateView, DetailView, DeleteView, CreateView, FormView, ListView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

class SubmittableLoginView(LoginView):
  template_name = 'registration/login.html'

class IndexView(TemplateView):
    template_name = "base.html"
    extra_context = {'students': Student.objects.all()}







