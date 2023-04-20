from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.http import HttpResponse
from django.template import Context,loader
from .models import Alumnos
from .models import Person
from .models import Profesores
# CRUD #####



def user_form(request):
    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_one')
    context = {'form':form}
    return render(request, 'form.html', context)



def update_user(request, pk):
    person = Person.objects.get(id = pk)
    form = PersonForm(instance=person)

    if request.metho == 'POST':
          form = PersonForm(request.POST, instance=person)
          if form.is_valid():
                form.save()
                return redirect('index_one')
    context = {'form':form}
    return render (request, 'form.html', context)


# ##########


def index(request):
#    template = loader.get_template('index.html')
#    return HttpResponse(template.render())
    context = {'students':ListaAlumnos,'teachers':ListaProfes}
    return render(request, 'index.html', context)




def student(request):
   
    contexto = {'estudiantes': ListaAlumnos}
    return render(request, 'students.html', contexto)


def teachers(request):
    
    context = {'profes': ListaProfes}
    return render(request,'teachers.html', context)






def estudiantes(request, pk):
    student_Obj = None
    for s in ListaAlumnos:
        if s['id'] == int(pk):
            student_Obj = s
    return render(request, 'student.html', {'stu':student_Obj})

def profesores(request, pk):
    profe_Obj = None
    for t in ListaProfes:
        if t['id'] == int(pk):
            profe_Obj = t
    return render(request, 'teacher.html', {'teach': profe_Obj})




ListaProfes = [
    {
        "id": 1,
        "name":"martin",
        "surname":"casco",
        "age": 44,
        "asignatura":"matemáticas",
    },
    {
        "id": 2,
        "name": "Manuel",
        "surname": "gorge",
        "age": 200,
        "asignatura":"historia",
    },
    {
        "id": 3,
        "name": "Joan",
        "surname": "Carles",
        "age": 3,
        "asignatura":"castellano",
    }]
# Lista Alumnos
ListaAlumnos = [
    {
        "id": 1,
        "name": "Eduardo",
        "surname": "Manos",
        "age": 99,
        "clase":"2",
    },
    {
        "id": 2,
        "name": "Paco",
        "surname": "Mendez",
        "age": 3,
        "clase":"10",
    },
    {
        "id": 3,
        "name": "Fernando",
        "surname": "Comida",
        "age": 1,
        "clase":"35",
    },
    {
        "id": 4,
        "name": "Miguel Angel",
        "surname": "Angel",
        "age": 30,
        "clase":"11",
    },
    {
        "id": 5,
        "name": "Michael",
        "surname": "John",
        "age": 11,
        "clase":"33",
    },
    {
        "id": 6,
        "name": "luisa",
        "surname": "nada",
        "age": 43,
        "clase":"5",
    }]