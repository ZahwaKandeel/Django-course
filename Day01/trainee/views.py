from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Trainee

# Create your views here.
def traineelist(request):
    context={"trainees":Trainee.objects.all()}
    return render(request,'trainee/traineeList.html',context)

def addTrainee(request):
    return HttpResponse('<h1>Add Trainee</h1>')

def updateTrainee(request):
    return HttpResponse('<h1>Update Trainee</h1>')

def deleteTrainee(request):
    return HttpResponse('<h1>Delete Trainee</h1>')

