from rest_framework import serializers
from Types.models import TypesModel


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesModel
        fields = "__all__"
