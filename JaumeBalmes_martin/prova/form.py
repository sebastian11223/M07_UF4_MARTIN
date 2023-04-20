from django import forms
from .models import Alumnos, Profesores


class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['name','surname', 'age', 'asignatura']


class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['name','surname', 'age', 'clase']

