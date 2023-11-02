from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from app.forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from app.models import Classroom, Student

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
        
        
def users_view(request):
    teachers = User.objects.filter(groups__name='Teacher')
    parents= User.objects.filter(groups__name='Parent')
    classrooms = Classroom.objects.all()
    students = Student.objects.all()
    return render(request, 'users.html', {'teachers': teachers, 'parents': parents, 'classrooms': classrooms, 'students': students})


