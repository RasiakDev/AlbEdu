from logging import getLogger
from django.shortcuts import render
from django.urls import reverse_lazy
from app.forms import ClassroomForm
from django.views.generic import CreateView, View, UpdateView
from app.models import Classroom
from django.contrib.auth.mixins import (
  LoginRequiredMixin, PermissionRequiredMixin
)

class ClassroomView(PermissionRequiredMixin, View):
    permission_required = "app.view_classroom"
    def get(self, request, *args, **kwargs):
        context = {'classrooms': Classroom.objects.all()}
        return render(request, "classrooms/classroom_view.html", context=context)
        
    
    
    
    
LOGGER = getLogger()
class ClassroomCreateView(CreateView):
    form_class = ClassroomForm
    template_name = 'classrooms/create_classroom.html'
    success_url = reverse_lazy('classrooms')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)
    

class ClassroomUpdateView(UpdateView):
      model = Classroom
      fields = '__all__'
      template_name = 'classrooms/create_classroom.html'
      success_url = reverse_lazy('classrooms')