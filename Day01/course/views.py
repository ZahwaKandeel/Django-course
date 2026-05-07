from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def courselist(request):
    context={"courses":Course.objects.all()}
    return render(request,'course/list.html',context)

def courseDetails(request,id):
    context={"course":Course.objects.get(pk=id)}
    return render(request, 'course/details.html', context)

def addCourse(request):
    if request.method == "POST":
        name = request.POST ["name"]
        code = request.POST ["code"]
        track = request.POST ["track"]

        Course.objects.create(name=name, code=code, track=track)
        return redirect ('courses')
    
    return render(request, 'course/add.html')

def updateCourse(request):
    return render(request, 'course/update.html')

def deleteCourse(request):
    return HttpResponse('<h1>Delete course</h1>')