from django.shortcuts import render, redirect  
from django.contrib.auth.models import User  
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages  
from django.db import IntegrityError  # Import IntegrityError  
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        task =  request.POST.get('task')
        new_todo = todo( user=request.user , todo_name =task )
        new_todo.save()
        
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos' :all_todos
    }
        
    return render(request , 'todoApp/todo.html' , context)

def registerPage(request): 
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':  
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        email = request.POST.get('email')  

        # Check for password length  
        if len(password) < 6:  
            messages.error(request, "Password must be at least 6 characters long")  
            return redirect('register-page')  

        if User.objects.filter(username=username).exists():  
            messages.error(request, "Sorry, that username is taken.")  
            return redirect('register-page')
        
        # Attempt to create the user  
        try:  
            new_user = User.objects.create_user(username=username, password=password, email=email)  
            new_user.save()  
            messages.success(request, "Registration successful! You can now log in.")  
            return redirect('login-page')  

        except IntegrityError:  
            # Handle the case where the username or email already exists  
            messages.error(request, "Sorry, that username or email is already taken.")  
            return redirect('register-page')  

    return render(request, 'todoApp/register.html', {})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        
        validate_user =  authenticate(username=username , password=password)
        
        if validate_user is not None :
            login(request , validate_user)
            return redirect('home-page')
        else:
            messages.error(request , "Invalid username or password")
            return redirect('login-page')
    
    return render(request , 'todoApp/login.html' , {})

@login_required
def DeleteTask(request , name):
    get_todo = todo.objects.get(user=request.user,todo_name = name)    
    get_todo.delete()
    return redirect('home-page')
    
def logoutPage(request):
    logout(request)
    return redirect('login-page')
    
def UpdateTask(request , name):
    get_todo = todo.objects.get(user=request.user,todo_name = name) 
    get_todo.status =  True  
    get_todo.save()
    
    return redirect('home-page')
        