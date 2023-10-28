from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, View, UpdateView, DetailView

from app.forms import ScheduleForm, PresenceForm
from app.models import Classroom, Schedule, Student, Present
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.auth.decorators import login_required


class ScheduleView(LoginRequiredMixin, PermissionRequiredMixin,View):
    permission_required = "app.view_schedule"
    def get(self, request, *args, **kwargs):
        context = {'schedules': Schedule.objects.all()}
        return render(request, "schedules/schedule_view.html", context=context)


class ScheduleProfile(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Schedule
    template_name = 'schedules/schedule_profile.html'
    permission_required = "app.view_schedule"

    def get_context_data(self, **kwargs):
        context = super(ScheduleProfile, self).get_context_data(**kwargs)
        presence_list = Present.objects.filter(schedule=self.object)
        context['students_id'] = [presence.student.id for presence in presence_list]
        context['presence_list'] = presence_list
        context['students'] = Student.objects.filter(classroom_id=self.object.classroom_id.id)
        return context


# add schedule time and classroom id
@login_required(redirect_field_name='login')

def schedule_form(request, classroom_id):
    classroom = Classroom.objects.get(pk=classroom_id)
    students = Student.objects.filter(classroom_id=classroom_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST)

        if form.is_valid():
            # Create and save the object
            start_hour = form.cleaned_data['start_hour']
            end_hour = form.cleaned_data['end_hour']

            new_object = Schedule.objects.create(classroom_id=classroom, start_hour=start_hour, end_hour=end_hour)
            new_object.save()
            return redirect('presence_list', schedule_id=new_object.id)  # Redirect to a success page
    else:
        form = ScheduleForm()
    return render(request, 'schedules/create_schedule.html',
                      {'classroom_id': classroom_id, 'form': form, 'students': students})



# show the list of students with the checkbox
@login_required(redirect_field_name='login')

def presence_list(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    students = Student.objects.filter(classroom_id=schedule.classroom_id.id)
    if request.method == 'POST':
        form = PresenceForm()
    else:
        form = PresenceForm()
    if request.user.is_authenticated:
        return render(request, 'schedules/presence_list.html',
                      {'schedule': schedule, 'students': students, 'form': form})
    else:
        return redirect('login')


# save the Present object
@login_required(redirect_field_name='login')
def presence_list_save(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    students = Student.objects.filter(classroom_id=schedule.classroom_id.id)
    if request.method == 'POST':
        selected_student_ids = request.POST.getlist('selected_students')
        selected_students = Student.objects.filter(id__in=selected_student_ids)
        not_selected_students = students.exclude(id__in=selected_students.values_list('id', flat=True))

        for student in selected_students:
            new_obj = Present.objects.create(schedule_id=schedule_id, student=student, is_present=True)
            new_obj.save()

        for student in not_selected_students:
            new_obj = Present.objects.create(schedule_id=schedule_id, student=student, is_present=False)
            new_obj.save()
        print("Not selected Students:", not_selected_students)

        # Do something with the selected students...
        print("Selected Student IDs:", selected_student_ids)
        print("Selected Students:", selected_students)

    return redirect('classrooms')  # Redirect to the student list view


def presence_list_update(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    students = Student.objects.filter(classroom_id=schedule.classroom_id.id)
    if request.method == 'POST':
        selected_student_ids = request.POST.getlist('selected_students')
        selected_students = Student.objects.filter(id__in=selected_student_ids)
        not_selected_students = students.exclude(id__in=selected_students.values_list('id', flat=True))

        for student in selected_students:
            try:
                current_presence_to_update = Present.objects.filter(schedule_id=schedule_id, student_id=student.id)
                current_presence_to_update.update(is_present=True)
            except:
                print("SELECTED STUDENTS DOES NOT EXIST---------------------")

        for student in not_selected_students:
            try:
                current_presence_to_update = Present.objects.filter(schedule_id=schedule_id, student_id=student.id)
                current_presence_to_update.update(is_present=False)
            except Present.DoesNotExist:
                print("NOT SELECTED STUDENTS DOES NOT EXIST-----------------")

        print("Not selected Students:", not_selected_students)

        # Do something with the selected students...
        print("Selected Student IDs:", selected_student_ids)
        print("Selected Students:", selected_students)

    return redirect('classrooms')  # Redirect to the student list view

