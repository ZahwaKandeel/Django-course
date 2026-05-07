from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Trainee

# Create your views here.
def traineelist(request):
    context={"traineesList":Trainee.objects.all()}
    return render(request,'trainee/list.html',context)

def traineeDetail(request,id):
    context = {"traineeDetails":Trainee.objects.get(pk=id)}
    return render(request, 'trainee/details.html', context)

def addTrainee(request):
    if request.method == "POST":
        Trainee.objects.create(name = request.POST ["name"], 
                               age = request.POST ["age"], 
                               degree = request.POST ["degree"],)
        return redirect ('traineesList')
    
    return render(request, 'trainee/add.html')

def updateTrainee(request, id):
    traineeUpd = Trainee.objects.get(pk=id)
    if request.method == "POST":
        traineeUpd.name = request.POST.get("name")
        traineeUpd.age = request.POST.get("age")
        traineeUpd.degree = request.POST.get("degree")

        traineeUpd.save()
        return redirect('traineeDetails', id=traineeUpd.id)

    return render(request, 'trainee/update.html', {"id":id})

def deleteTrainee(request):
    return HttpResponse('<h1>Delete Trainee</h1>')

