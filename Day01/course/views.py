from django.shortcuts import HttpResponse

# Create your views here.
def courselist(request):
    return HttpResponse('<h1>Trainee course</h1>')

def addCourse(request):
    return HttpResponse('<h1>Add course</h1>')

def updateCourse(request):
    return HttpResponse('<h1>Update course</h1>')

def deleteCourse(request):
    return HttpResponse('<h1>Delete course</h1>')