from django.shortcuts import render
from django.urls import reverse_lazy
from app.forms import ScheduleForm
from django.views.generic import CreateView, View, UpdateView, DetailView
from app.models import Schedule
from django.contrib.auth.mixins import (
  LoginRequiredMixin, PermissionRequiredMixin
)

class ScheduleView(View):
    def get(self, request, *args, **kwargs):
        context = {'schedules': Schedule.objects.all()}
        return render(request, "schedules/schedule_view.html", context=context)
        
class ScheduleProfile(DetailView):
    model = Schedule
    template_name = 'schedules/schedule_profile.html'

    
class CreateScheduleView(CreateView):
    form_class = ScheduleForm
    template_name='schedules/create_schedule.html'
    success_url = reverse_lazy('schedules')