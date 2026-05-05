from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def courselist(request):
    courses = {
        '1':{    'id':1,  'name':'css'  },
        '2':{    'id':2,  'name':'django'  }
    }

    course = [1,'css','css course']

    context={
        'Name':'Courses names',
        'courses':courses,
        'course':course}
    
    return render(request,'course/courseList.html',context)

def addCourse(request):
    return HttpResponse('<h1>Add course</h1>')

def updateCourse(request):
    return HttpResponse('<h1>Update course</h1>')

def deleteCourse(request):
    return HttpResponse('<h1>Delete course</h1>')