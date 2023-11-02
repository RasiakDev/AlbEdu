from logging import getLogger
from django.shortcuts import render
from django.urls import reverse_lazy
from app.forms import ClassroomForm
from django.views.generic import CreateView, View, UpdateView, DetailView, DeleteView
from app.models import Classroom, Schedule
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)


class ClassroomView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "app.view_classroom"

    def get(self, request, *args, **kwargs):
        context = {'classrooms': Classroom.objects.all()}
        return render(request, "classrooms/classroom_view.html", context=context)


class ClassroomProfile(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'classrooms/classroom_profile.html'
    model = Classroom
    permission_required = "app.view_classroom"

    def get_context_data(self, *args, **kwargs):
        context = super(ClassroomProfile,
                        self).get_context_data(*args, **kwargs)
        # add extra field
        id = self.kwargs['pk']
        context["schedules"] = Schedule.objects.filter(classroom_id=id).order_by('-created', '-start_hour')
        return context


LOGGER = getLogger()


class ClassroomCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    form_class = ClassroomForm
    template_name = 'classrooms/create_classroom.html'
    success_url = reverse_lazy('classrooms')
    permission_required = "app.add_classroom"

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class ClassroomUpdateView(LoginRequiredMixin, UpdateView):
    model = Classroom
    fields = '__all__'
    template_name = 'classrooms/create_classroom.html'
    success_url = reverse_lazy('classrooms')


class ClassroomDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Classroom
    template_name = 'form_confirm_delete.html'
    success_url = reverse_lazy('classrooms')
    permission_required='app.delete_classroom'
