from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Course

# Create your views here.
def courselist(request):
    context={"courses":Course.objects.all()}
    return render(request,'course/courseList.html',context)

def courseDetails(request):
    context={"Details":Course.objects.get(pk=id)}
    return render(request, 'course/deatils.html',context)

def addCourse(request):
    return HttpResponse('<h1>Add course</h1>')

def updateCourse(request):
    return HttpResponse('<h1>Update course</h1>')

def deleteCourse(request):
    return HttpResponse('<h1>Delete course</h1>')