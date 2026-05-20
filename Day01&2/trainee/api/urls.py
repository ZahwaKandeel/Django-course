from rest_framework.routers import DefaultRouter
from .views import TraineeViewSet
from django.urls import path,include

router = DefaultRouter()
router.register('trainees', TraineeViewSet, basename='trainee')

urlpatterns = [
    path('',include(router.urls)),
]