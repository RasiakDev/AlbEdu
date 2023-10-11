from django.urls import path, include
from app.views.views import IndexView, SubmittableLoginView
from app.views.students_view import StudentCreateView, StudentUpdateView, StudentDeleteView, student_view
from app.views.classroom_view import ClassroomCreateView, ClassroomView, ClassroomUpdateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('student/', student_view, name='student'),
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name="delete_student"),
    path('student/create', StudentCreateView.as_view(), name='create_student' ),
    path('student/update/<int:pk>', StudentUpdateView.as_view(), name='update_student'),
    path('classrooms/', ClassroomView.as_view(), name='classrooms'),
    path('classroom/create', ClassroomCreateView.as_view(), name='create_classroom'),
    path('classroom/update/<int:pk>', ClassroomUpdateView.as_view(), name='update_classroom'),
]   
