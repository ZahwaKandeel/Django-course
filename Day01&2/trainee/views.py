from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm, TraineeFormModel
from course.models import Course
from django.views import generic, View
from django.contrib.auth.decorators import login_required

# Create your views here.
#def traineelist(request):
#    context={"traineesList":Trainee.objects.filter(is_active=True)}
#    return render(request,'trainee/list.html',context)

#Generic View
class TraineeListView(generic.ListView):
    queryset = Trainee.objects.filter(is_active=True)
    template_name = 'trainee/list.html'
    context_object_name = 'traineesList'

def traineeDetail(request,id):
    context = {"traineeDetails":Trainee.objects.get(pk=id)}
    return render(request, 'trainee/details.html', context)

# def addTrainee(request):
#     if request.method == "POST":
#         Trainee.objects.create(name = request.POST ["name"], 
#                                age = request.POST ["age"], 
#                                degree = request.POST ["degree"],)
#         return redirect ('traineesList')

#     return render(request, 'trainee/add.html')

def updateTrainee(request, id):
    traineeUpd = Trainee.objects.get(pk=id)
    if request.method == "POST":
        traineeUpd.name = request.POST.get("name")
        traineeUpd.age = request.POST.get("age")
        traineeUpd.degree = request.POST.get("degree")

        traineeUpd.save()
        return redirect('traineeDetails', id=traineeUpd.id)

    return render(request, 'trainee/update.html', {"id":id})

def deleteTrainee(request,id):
    traineeDel = Trainee.objects.get(pk=id)
    if request.method == "POST":
        traineeDel.name = request.POST.get("name")
        traineeDel.code = request.POST.get("age")
        traineeDel.track = request.POST.get( "degree")
        
        traineeDel.delete()
        return redirect('traineesList')    

    return render(request, 'trainee/delete.html', {"traineeDel":traineeDel})

# def addTraineeForm(request):
#     context = {"trainees": Trainee.objects.all(), 'form':TraineeForm()}
#     if request.method == "POST":
#         form = TraineeForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             Trainee.objects.create(
#                 name = request.POST ["name"], 
#                 age = request.POST ["age"], 
#                 degree = request.POST ["degree"],
#                 image = request.FILES.get("image"),
#                 course = Course.objects.get(pk = request.POST["course"])
#             )
#             return redirect('traineesList')
#         else:
#             print(form.errors)
#     return render(request, "trainee/add.html", context=context)

# def addTraineeModelForm(request):
#     context = {"trainees": Trainee.objects.all(), 'form':TraineeFormModel()}
#     if request.method == "POST":
#         form = TraineeFormModel(data=request.POST, files=request.FILES)
#         if form.is_valid:
#             form.save()
#             return redirect('traineesList')
#     return render(request, "trainee/add.html", context=context)

def deleteTraineeSoft(request,id):
    traineeDel = Trainee.objects.get(pk=id)
    if request.method == "POST":
        traineeDel.is_active = False
        traineeDel.save()
        return redirect('traineesList')
    return render(request, 'trainee/delete.html', {"traineeDel":traineeDel})


#insert trainee class based view
class AddTraineeView(View):
    def get(self, request):
        form=TraineeFormModel()
        return render(request, "trainee/add.html", {"form":form})

    def post(self, request):
        form = TraineeFormModel(data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect('traineesList')
        return render(request, "trainee/add.html", {"form":form})   
    
#insert trainee generic with model form
class AddTraineeModelFormView(generic.CreateView):
    model = Trainee
    form_class = TraineeFormModel
    template_name = "trainee/add.html"
    success_url = "Trainee/trainees/"

@login_required(login_url='/login/')
def secretPage(request):
    return render(request, 'accounts/secret.html')