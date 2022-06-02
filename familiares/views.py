# from tkinter.tix import Tree
from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.


def familiares1(request):
    nuevo_familiar = Familiares.objects.create(
        dni=36420295,
        nombre='Javier',
        apellido='Deheza',
        edad=31,
        hijos=11,
        activo=True)
    
# def familiares_add(request):
#     new_familiares = familiares.objects.all()
#     context = {'new_familiares':new_familiares}
#     return render(request,'index.html',context=context)

# {% for familia in new_familiares %}
   
#         {{familia.nombre}}<br>

#       {% endfor %}

    context = {'nuevo_familiar': nuevo_familiar}
    return render(request, 'familiares.html', context=context)
