from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,loader

def index(request):
    professor = {"name":"Martín", "surname":"Casco", "age":"20"}
    template = loader.get_template('index.html')
    dades = template.render({'nombre':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})
    return HttpResponse(dades)

def student(request):
    estudiantes = {"name":"Pepe", "surname":"Perales", "age":"25", "clase":"2"}
    contexto = {'estudiantes': estudiantes}
    return render(request, 'students.html', contexto)

def teachers(request):
    profesores = {"name":"Juan", "surname":"Ronda", "age":"50", "asignatura":"matemáticas"}
    context = {'profes': profesores}
    return render(request,'teachers.html', context)
