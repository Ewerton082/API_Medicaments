from rest_framework import serializers
from Brands.models import BrandsModel


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandsModel
        fields = "__all__"
