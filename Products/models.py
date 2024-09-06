from django.db import models
from Brands.models import BrandsModel
from Types.models import TypesModel

# Create your models here.


class ProductsModel(models.Model):
    name = models.CharField(max_length=100)
    brands = models.ForeignKey(to=BrandsModel, on_delete=models.PROTECT, related_name='brands')
    type_product = models.ForeignKey(to=TypesModel, on_delete=models.PROTECT, related_name='types')
    how_use = models.TextField(max_length=500, null=True, blank=True)
    idea_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"