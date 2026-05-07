from django.urls import path
from trainee.views import *

urlpatterns = [
    path('trainees/', traineelist, name='traineesList'),
    path('traineeDetails/<int:id>/', traineeDetail, name='traineeDetails'),
    path('add/', addTrainee, name='addTrainee'),
    path('update/<int:id>/', updateTrainee, name='updateTrainee'),
    path('delete/', deleteTrainee, name='deleteTrainee'),
]