from django.urls import path, include
from app.views.views import IndexView, SubmittableLoginView
from app.views.students_view import StudentCreateView, StudentUpdateView, StudentDeleteView, student_view, StudentProfile
from app.views.classroom_view import ClassroomCreateView, ClassroomView, ClassroomUpdateView
from app.views.schedule_view import ScheduleView, CreateScheduleView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),

    path('students/', student_view, name='student'),
    path('student/<int:pk>', StudentProfile.as_view(), name='student_profile'),
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name="delete_student"),
    path('student/create', StudentCreateView.as_view(), name='create_student' ),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='update_student'),
    
    path('classrooms/', ClassroomView.as_view(), name='classrooms'),
    path('classroom/create', ClassroomCreateView.as_view(), name='create_classroom'),
    path('classroom/update/<int:pk>', ClassroomUpdateView.as_view(), name='update_classroom'),

    path('schedules/', ScheduleView.as_view(), name='schedules'),
    path('schedules/create', CreateScheduleView.as_view(), name='create_schedule'),
]   
