from rest_framework import serializers
from Products.models import ProductsModel
from Types.serializers import TypeSerializer
from Brands.serializers import BrandSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = "__all__"


class ProductSerializerPretty(serializers.ModelSerializer):
    brands = BrandSerializer()
    type_product = TypeSerializer()

    class Meta:
        model = ProductsModel
        fields = ['id', 'type_product', 'name', 'brands', 'idea_price', 'how_use']
