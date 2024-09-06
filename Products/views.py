from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Products.models import ProductsModel
from Products.serializers import ProductSerializer
from django.http import JsonResponse

# Create your views here.


class ListCreateProducts(ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer


class DetailUpdateDeleteProducts(RetrieveUpdateDestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        instance = self. get_object()

        try:
            instance.delete()
            return JsonResponse({'message': 'dados deletado com sucesso'},
                                status=204)

        except Exception as error:
            return JsonResponse({'error': f"Algo deu errado: {str(error)}"},
                                status=500)
