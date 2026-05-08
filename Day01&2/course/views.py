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

def updateCourse(request,id):
    courseUpd = Course.objects.get(pk=id)
    if request.method == "POST":
        courseUpd.name = request.POST.get("name")
        courseUpd.code = request.POST.get("code")
        courseUpd.track = request.POST.get( "track")

        courseUpd.save()
        return redirect('coursesDetails', id=courseUpd.id)

    return render(request, 'course/update.html', {"id":id})

def deleteCourse(request,id):
    courseDel = Course.objects.get(pk=id)
    if request.method == "POST":
        courseDel.name = request.POST.get("name")
        courseDel.code = request.POST.get("code")
        courseDel.track = request.POST.get( "track")
        
        courseDel.delete()
        return redirect('courses')    

    return render(request, 'course/delete.html', {"courseDel":courseDel})