from django.db import models

# Create your models here.


class PiezaSoldadura(models.Model):

    Code=models.CharField(max_length=40)
    Client=models.CharField(max_length=40)
    Cadencia=models.CharField(max_length=40)
    NumDoc=models.CharField(max_length=40) 
    


class PiezaPrensa(models.Model):

    Code=models.CharField(max_length=100, null=True)
    Client=models.CharField(max_length=100, null=True)
    Cadencia = models.CharField(max_length=100, null=True)
    NumDoc=models.CharField(max_length=100, null=True) 


class DeclararPieza(models.Model):

    Code=models.CharField(max_length=40)
    Client=models.CharField(max_length=40)
    Cadencia=models.CharField(max_length=40)
    NumDoc=models.CharField(max_length=40) 
    Cantidad=models.CharField(max_length=40) 
    Horas=models.CharField(max_length=40) 