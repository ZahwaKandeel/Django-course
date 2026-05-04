from django.http.response import HttpResponse

# Create your views here.
def traineelist(request):
    return HttpResponse('<h1>Trainee List</h1>')

def addTrainee(request):
    return HttpResponse('<h1>Add Trainee</h1>')

def updateTrainee(request):
    return HttpResponse('<h1>Update Trainee</h1>')

def deleteTrainee(request):
    return HttpResponse('<h1>Delete Trainee</h1>')