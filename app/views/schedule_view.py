from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, UpdateView, DetailView

from app.forms import ScheduleForm, PresenceForm
from app.models import Classroom, Schedule, Student, Present
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


def schedule_form(request, classroom_id):
    classroom= Classroom.objects.get(pk = classroom_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST)

        if form.is_valid():
            # Create and save the object
            start_hour = form.cleaned_data['start_hour']
            end_hour = form.cleaned_data['end_hour']

            new_object = Schedule.objects.create(classroom_id=classroom, start_hour=start_hour, end_hour=end_hour)
            new_object.save()
            return redirect('presence_list', schedule_id = new_object.id)  # Redirect to a success page
    else:
        form = ScheduleForm()
    return render(request, 'schedules/create_schedule.html', {'classroom_id': classroom_id, 'form': form})


def presence_list(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    students = Student.objects.filter(classroom_id = schedule.classroom_id.id)

    form = PresenceForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            for student in students:
                # is_present = form.cleaned_data.get(str(student.id), False)
                presence = form.cleaned_data.get(f'is_selected_{student.id}', False)                # student.save()
                print(f'+++++{presence}----{student}')
                new_student = Present.objects.create(student=student, schedule=schedule, presence=presence)
                new_student.save()
            return redirect('classrooms')


    return render(request, 'schedules/presence_list.html',{'schedule': schedule, 'students': students} )


def presence_list_save(request):
    if request.method == 'POST':
        selected_student_ids = request.POST.getlist('selected_students')
        selected_students = Student.objects.filter(id__in=selected_student_ids)

        # Do something with the selected students...
        print("Selected Student IDs:", selected_student_ids)
        print("Selected Students:", selected_students)

    return redirect('classrooms')  # Redirect to the student list view
