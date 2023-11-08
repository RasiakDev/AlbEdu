from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages
from django.urls import reverse_lazy  
from app.forms import RegisterForm, UpdateUserForm
from django.contrib.auth.models import User, Group
from app.models import Classroom, Student
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)


@login_required(redirect_field_name='login')
@permission_required("auth.add_user")
def register_teacher(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            teacher_group = Group.objects.get(name='Teacher')
            teacher_group.user_set.add(user)
            # login(request, user)
            return redirect('users')
        else:
            return render(request, 'registration/register.html', {'form': form})
        
@login_required(redirect_field_name='login')
@permission_required("auth.add_user")
def register_parent(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            parent_group = Group.objects.get(name='Parent')
            parent_group.user_set.add(user)
            return redirect('users')
        else:
            return render(request, 'registration/register.html', {'form': form})
        
@login_required(redirect_field_name='login')
@permission_required("auth.view_user")
def users_view(request):
    teachers = User.objects.filter(groups__name='Teacher')
    parents= User.objects.filter(groups__name='Parent')
    classrooms = Classroom.objects.all()
    students = Student.objects.all()
    return render(request, 'users.html', {'teachers': teachers, 'parents': parents, 'classrooms': classrooms, 'students': students})



class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/register.html'
    fields = '__all__'
    success_url = reverse_lazy('users')
    permission_required = 'auth.change_user'

@login_required(login_url='login')
@permission_required("auth.delete_user")
def del_user(request, id):
    user = User.objects.get(id=id) # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        user.delete()
        # redirect to the bands list
        return redirect('users')

    # no need for an `else` here. If it's a GET request, just continue

    return render(request,
                    'registration/confirm_delete_user.html',
                    {'user': user})


@login_required(login_url='lodin')
@permission_required('auth.change_user')
def update_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users')
    else:
        user_form = UpdateUserForm(instance=user)

    return render(request, 'registration/update_user.html', {'form': user_form})