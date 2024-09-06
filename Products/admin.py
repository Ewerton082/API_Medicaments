from django.contrib import admin
from Products.models import ProductsModel

# Register your models here.


@admin.register(ProductsModel)
class ProductsAdmin(admin.ModelAdmin):
    model = ProductsModel
    list_display = ["type_product", "name", "brands", "idea_price", "how_use"]