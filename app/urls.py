from django.urls import path, include
from app.views.views import IndexView, ParentView, StudentUpdateView, SubmittableLoginView, ParentDeleteView, StudentCreateView, StudentView, StudentDeleteView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('parent/<int:pk>', ParentView.as_view(), name="parent"),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('parent/delete/<int:pk>', ParentDeleteView.as_view(), name='delete_parent' ),
    path('student/', StudentView.as_view(), name='student'),
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name="delete_student"),
    path('student/create', StudentCreateView.as_view(), name='create_student' ),
    path('student/update<int:pk>', StudentUpdateView.as_view(), name='update_student')
    

    # path('login/', LoginView(template_name='login_form.html').as_view(), name='login')
]
