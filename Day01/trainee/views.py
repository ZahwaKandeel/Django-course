from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def traineelist(request):
    trainees={'1':{    'id':1,  'name':'zahwa'  },
              '2':{    'id':2,  'name':'ahmed'  }}
    trainee=[1,'Zahwa','track python']
    context={'Name':'Trainess names','trainees':trainees,'trainee':trainee}
    
    return render(request,'trainee/traineeList.html',context)

def addTrainee(request):
    return HttpResponse('<h1>Add Trainee</h1>')

def updateTrainee(request):
    return HttpResponse('<h1>Update Trainee</h1>')

def deleteTrainee(request):
    return HttpResponse('<h1>Delete Trainee</h1>')

