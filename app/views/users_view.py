from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from app.forms import RegisterForm  
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from app.models import Classroom

def sign_up(request):
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
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/register.html', {'form': form})
        
def users_view(request):
    teachers = User.objects.filter(groups__name='Teacher')
    parents= User.objects.filter(groups__name='Parent')
    classrooms = Classroom.objects.all()
    return render(request, 'users.html', {'teachers': teachers, 'parents': parents, 'classrooms': classrooms})