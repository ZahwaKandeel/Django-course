from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'users/base.html')

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')