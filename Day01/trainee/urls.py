from django.urls import path
from trainee.views import *

urlpatterns = [
    path('traineelist/', traineelist, name='traineelist'),
    path('add/', addTrainee, name='addTrainee'),
    path('update', updateTrainee, name='updateTrainee'),
    path('delete', deleteTrainee, name='deleteTrainee'),
]