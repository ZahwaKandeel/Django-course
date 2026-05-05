from django.urls import path
from course.views import *

urlpatterns = [
    path('courses/', courselist, name='Courses'),
    path('coursesDetails/', courseDetails, name='courseDetails'),
    path('add/', addCourse, name='addCourse'),
    path('update/', updateCourse, name='updateCourse'),
    path('delete/', deleteCourse, name='deleteCourse'),
]