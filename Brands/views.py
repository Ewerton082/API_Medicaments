from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from Brands.models import BrandsModel
from Brands.serializers import BrandSerializer
from django.http import JsonResponse
from API.permissions import GlobalPermissions

# Create your views here.


class ListCreateBrands(ListCreateAPIView):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated, GlobalPermissions)


class DetailUpdateDeleteBrands(RetrieveUpdateDestroyAPIView):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated, GlobalPermissions)

    def delete(self, request, *args, **kwargs):
        instance = self. get_object()

        try:
            instance.delete()
            return JsonResponse({'message': 'dados deletado com sucesso'},
                                status=204)

        except Exception as error:
            return JsonResponse({'error': f"Algo deu errado: {str(error)}"},
                                status=500)
