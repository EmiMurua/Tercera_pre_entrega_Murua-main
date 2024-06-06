from django import forms

class SoldaduraForm(forms.Form):
    Code = forms.CharField(max_length=40, label="Codigo de pieza:")
    Client = forms.CharField(max_length=40, label="Cliente:")
    Cadencia = forms.CharField(max_length=40, label="Cadencia")
    NumDoc = forms.CharField(max_length=40, label="Numero de documento") 
    

class PrensaForm(forms.Form):
    Code = forms.CharField(max_length=40, label="Codigo de pieza:")
    Client = forms.CharField(max_length=40, label="Cliente:")
    Cadencia = forms.CharField(max_length=40, label="Cadencia")
    NumDoc = forms.CharField(max_length=40, label="Numero de documento") 


class SearchForm(forms.Form):
    Piezas = [
        ('Soldadura', 'Soldadura'),
        ('Prensa', 'Prensa'),
    ]
    tipo = forms.ChoiceField(choices=Piezas, label="Seleccione el tipo de pieza:")
    Code = forms.CharField(max_length=40, label="Ingrese el código de la pieza:")

