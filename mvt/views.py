from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render 

def bienvenido(request):
    return HttpResponse ('en esta web podras ver informacion de la familia')

def autor(request):
    context= {'nombre':'mariano', 'apellido':'deheza'}
    
    return render(request, 'plantilla1.html', context= context )