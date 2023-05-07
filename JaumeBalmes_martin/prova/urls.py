from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('index2', views.index, name='index'),
    path('students', views.student, name='students'),
    path('teachers', views.teachers, name='teachers'),
    path('teacher/<str:pk>/', views.profesores, name='teacher'),
    path('student/<str:pk>/', views.estudiantes, name='student'),
    path('update-user/<str:pk>/', views.update_user, name='update-user'),
    path('user-form/', views.user_form, name='user_form'),
    # path('', views.students, name='students')
]

