from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from Products.models import ProductsModel
from Products.serializers import ProductSerializer, ProductSerializerPretty
from django.http import JsonResponse

# Create your views here.


class ListCreateProducts(ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductSerializerPretty
        return ProductSerializer


class DetailUpdateDeleteProducts(RetrieveUpdateDestroyAPIView):
    queryset = ProductsModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductSerializerPretty
        return ProductSerializer

    def delete(self, request, *args, **kwargs):
        instance = self. get_object()

        try:
            instance.delete()
            return JsonResponse({'message': 'dados deletado com sucesso'},
                                status=204)

        except Exception as error:
            return JsonResponse({'error': f"Algo deu errado: {str(error)}"},
                                status=500)
