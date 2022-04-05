from datetime import datetime
from django.template import loader
from django.shortcuts import render
from aplicoder.models import Familia
from aplicoder.forms import Dato

# Create your views here.

def inicio(request):
    return render(request,'aplicoder/index.html')

def family(request):
    if request.method=='POST':
        familiaridad=Dato(request.POST)
        print(familiaridad)
        print("pasastee los dastos a familiaridad\n")
        if familiaridad.is_valid():
            print("\nentraste")
            datos=familiaridad.cleaned_data
            print("\npasaste el cleaned data")
            datos=Familia(nombre=datos['Nombre'],dni=datos['dni'])
            datos.save()
        return render(request, "aplicoder/familiares.html", {"familia": family, "title": "familia", "page": "familia", "formulario": familiaridad})
    else:
        familiaridad=Dato()
        return render(request, "aplicoder/familiares.html", {"familia": family, "title": "familia", "page": "familia", "formulario": familiaridad})
