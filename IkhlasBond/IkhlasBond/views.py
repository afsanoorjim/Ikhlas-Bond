from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse


def landing(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=name, email=email, password=password)
        user.save()
        messages.success(request,"User Created Successfully")
        return render(request, 'landing.html')
    return render(request, 'landing.html')