from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from user.views import user_dashboard

def landing(request):
    return render(request, 'landing.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=name, email=email, password=password)
        user.save()
        messages.success(request,"User Created Successfully")
        return redirect(landing)
    messages.info(request, 'Problem Detected')
    return redirect(landing)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(f"Attempting to authenticate user with email: {email}")  # Debug statement
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print(f"User with email {email} does not exist")
        if user is not None:
            user = authenticate(request, email=email, password=password)
            print(f"Authentication successful for user: {user}")  # Debug statement
            auth_login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect(user_dashboard)
        else:
            print("Authentication failed")  # Debug statement
        messages.success(request, "Problem Detected")
        return redirect(landing)