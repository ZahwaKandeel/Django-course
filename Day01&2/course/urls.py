from django.urls import path
from course.views import *

urlpatterns = [
    path('courses/', courselist, name='courses'),
    path('coursesDetails/<int:id>/', courseDetails, name='coursesDetails'),
    path('add/', addCourse, name='addCourse'),
    path('update/<int:id>/', updateCourse, name='updateCourse'),
    path('delete/<int:id>/', deleteCourse, name='deleteCourse'),
]