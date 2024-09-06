from django.urls import path
from Products.views import ListCreateProducts, DetailUpdateDeleteProducts

urlpatterns = [
    path('products/', ListCreateProducts.as_view(), name='List and Create products'),
    path('products/<int:pk>', DetailUpdateDeleteProducts.as_view(), name="update, detail and delete")
]