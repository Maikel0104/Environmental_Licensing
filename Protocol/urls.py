from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    
    path('menu/', views.menu_principal, name='menu_principal'),

    path('licencas/', views.historico_licencas, name='historico_licencas'),

    path('denuncias/', views.historico_denuncias, name='historico_denuncias'),

    path('novo_pedido/', views.novo_pedido, name='novo_pedido'),
]