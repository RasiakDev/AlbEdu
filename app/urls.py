from django.urls import path, include
from app.views.views import IndexView, SubmittableLoginView
from app.views.students_view import StudentCreateView, StudentUpdateView, StudentDeleteView, student_view, StudentProfile
from app.views.classroom_view import ClassroomCreateView, ClassroomView, ClassroomUpdateView, ClassroomProfile, ClassroomDeleteView
from app.views.schedule_view import ScheduleView, ScheduleProfile, schedule_form, presence_list, presence_list_save,presence_list_update
from django.contrib.auth.views import LogoutView
from app.views.users_view import sign_up, users_view


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('accounts/register/teacher', sign_up, name='register_teacher'),

    path('students/', student_view, name='student'),
    path('student/<int:pk>', StudentProfile.as_view(), name='student_profile'),
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name="delete_student"),
    path('student/create', StudentCreateView.as_view(), name='create_student' ),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='update_student'),
    
    path('classrooms/', ClassroomView.as_view(), name='classrooms'),
    path('classroom/<int:pk>', ClassroomProfile.as_view(), name='classroom_profile'),
    path('classroom/create', ClassroomCreateView.as_view(), name='create_classroom'),
    path('classroom/update/<int:pk>', ClassroomUpdateView.as_view(), name='update_classroom'),
    path('classroom/delete/<int:pk>', ClassroomDeleteView.as_view(), name='delete_classroom'),

    path('schedules/', ScheduleView.as_view(), name='schedules'),
    path('schedule/<int:pk>', ScheduleProfile.as_view(), name='schedule_profile'),
    path('schedules/create/<int:classroom_id>', schedule_form, name='create_schedule'),
    path('schedules/create/presence_list/<int:schedule_id>', presence_list, name='presence_list'),
    path('schedules/create/presence_list_save/<int:schedule_id>', presence_list_save, name='presence_list_save'),
    path('schedules/create/presence_list_update/<int:schedule_id>', presence_list_update, name='presence_list_update'),

    path('users/', users_view, name='users')


    ]


