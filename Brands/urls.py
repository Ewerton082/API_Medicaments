from django.urls import path
from Brands.views import ListCreateBrands, DetailUpdateDeleteBrands

urlpatterns = [
    path('brands/', ListCreateBrands.as_view(), name="Listar e Criar Brands"),
    path('brands/<int:pk>/', DetailUpdateDeleteBrands.as_view(), name="detalhes, update e delete"),
]
