# from tkinter.tix import Tree
from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.


def familiares1(request):
    tablafamilia = Familiares.objects.all()
    context = {'tablafamilia': tablafamilia}
    return render(request, 'familiares.html', context=context) 
    



  
