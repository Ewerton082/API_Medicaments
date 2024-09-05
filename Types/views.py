from rest_framework import generics
from Types.serializers import TypeSerializer
from Types.models import TypesModel
from django.http import JsonResponse

# Create your views here.


class ListCreateTypes(generics.ListCreateAPIView):
    serializer_class = TypeSerializer
    queryset = TypesModel.objects.all()


class DetailUpdateDeleteTypes(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TypeSerializer
    queryset = TypesModel.objects.all()

    def delete(self, request, *args, **kwargs):
        istance = self.get_object()

        try:
            istance.delete()
            return JsonResponse({'message': "Dados deletados com sucesso"},
                                status=204)

        except Exception as error:
            return JsonResponse({'message': f"Houve um erro:{error}"},
                                status=500)
