from django.urls import path
from . import views


urlpatterns = [
    
    path('menu/', views.menu_principal, name='menu_principal'),

    path('licencas/', views.historico_licencas, name='historico_licencas'),

    path('denuncias/', views.historico_denuncias, name='historico_denuncias'),

    path('novo_pedido/', views.novo_pedido, name='novo_pedido'),
]