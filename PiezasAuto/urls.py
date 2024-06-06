from django.urls import path

from PiezasAuto import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Agregar_pieza_soldadura/', views.Agregar_nueva_piezaS, name='Agregar_nueva_piezaS'),
    path('Agregar_pieza_prensa/', views.Agregar_nueva_piezaP, name='Agregar_nueva_piezaP'),
    path('buscar_pieza/', views.Search_Pieza, name='Search_Pieza'),
    path('Lista_piezas_soldadura/', views.Lista_piezas_sold, name='Lista_piezas_sold'),
    path('Lista_piezas_prensas/', views.Lista_piezas_prensas, name='Lista_piezas_prensas')
]