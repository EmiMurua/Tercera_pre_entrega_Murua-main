from django.shortcuts import render
from .models import *
from .forms import *

def home(req):
    return render(req, 'home.html')

def Lista_piezas_sold(req):

  list = PiezaSoldadura.objects.all()

  return render(req, "Lista_piezas_sold.html", {"Lista_piezas_soldadura": list})

def Lista_piezas_prensas(req):

  list = PiezaPrensa.objects.all()

  return render(req, "Lista_piezas_prensas.html", {"Lista piezas de prensas": list})

def Agregar_nueva_piezaS(req):
    if req.method == "POST":
        form = SoldaduraForm(req.POST)
        if form.is_valid():
            SoldaduraForm.objects.create(
                Code=form.cleaned_data['Code'],
                Client=form.cleaned_data['Client'],
                Cadencia=form.cleaned_data['Cadencia'],
                NumDoc=form.cleaned_data['NumDoc']
            )
            return render(req, 'home.html')  
    else:
        form = SoldaduraForm()
    return render(req, 'Search_Pieza.html', {'form': form}) 

def Agregar_nueva_piezaP(req):
    if req.method == "POST":
        form = PrensaForm(req.POST)
        if form.is_valid():
            PiezaPrensa.objects.create(
                Code=form.cleaned_data['Code'],
                Client=form.cleaned_data['Client'],
                Cadencia=form.cleaned_data['Cadencia'],
                NumDoc=form.cleaned_data['NumDoc']
            )
            return render(req, 'home.html')  
    else:
        form = PrensaForm()
    return render(req, 'Search_Pieza.html', {'form': form}) 


def Search_Pieza(req):
    if req.method == "POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            Client = form.cleaned_data['Client']
            Code = form.cleaned_data['Code']
            if Client == 'Soldadura':
                resultados = PiezaSoldadura.objects.filter(Code__icontains=Code)
            else:
                resultados = PiezaPrensa.objects.filter(Code__icontains=Code)
            return render(req, 'resultados.html', {'resultados': resultados})
    else:
        form = SearchForm()
    return render(req, 'Search_Pieza.html', {'form': form})