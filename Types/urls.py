from django.urls import path
from Types.views import ListCreateTypes, DetailUpdateDeleteTypes

urlpatterns = [
    path('types/', ListCreateTypes.as_view(), name="Listar e Criar"),
    path('types/<int:pk>', DetailUpdateDeleteTypes.as_view(), name="Detalhes, Editar e Apagar"),
]
