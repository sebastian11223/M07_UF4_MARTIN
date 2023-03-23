from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def student(request):
    template = loader.get_template('students.html')
    return HttpResponse(template.render())

def teachers(request):
    template = loader.get_template('students.html')
    return HttpResponse(template.render())
