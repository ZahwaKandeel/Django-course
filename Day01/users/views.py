from django.shortcuts import render
from django.contrib.auth import logout as auth_logout

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def logout(request):
    auth_logout(request)
    return render(request, 'users/logout.html')