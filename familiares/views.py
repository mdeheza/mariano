# from tkinter.tix import Tree
from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.


def familiares1(request):
    nuevo_familiar = Familiares.objets.create(
        dni=36420295,
        nombre='Javier',
        apellido='Deheza',
        edad=31,
        hijos=11,
        activo=True)

    context = {'nuevo_familiar': nuevo_familiar}
    return render(request, 'familiares.html', context=context)
