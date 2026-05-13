from django.urls import path
from trainee.views import *

urlpatterns = [
    #path('trainees/', traineelist, name='traineesList'),
    path('trainees/', TraineeListView.as_view(), name='traineesList'),
    path('traineeDetails/<int:id>/', traineeDetail, name='traineeDetails'),
    # path('add/', addTrainee, name='addTrainee'),
    path('update/<int:id>/', updateTrainee, name='updateTrainee'),
    path('delete/<int:id>/', deleteTrainee, name='deleteTrainee'),
    # path('addForm/', addTraineeForm, name="addTraineeForm"),
    # path('addModelForm/', addTraineeModelForm, name="addTraineeModelForm"),
    path('deleteSoft/<int:id>/', deleteTraineeSoft, name="deleteTraineeSoft"),
    path('addForm/', AddTraineeView.as_view(), name="addTraineeForm")
]