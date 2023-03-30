from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('index2', views.index, name='index'),
    path('students', views.student, name='student'),
    path('teachers', views.teachers, name='teachers')
    
    # path('', views.students, name='students')
]
