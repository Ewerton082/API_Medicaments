from django.contrib import admin
from Brands.models import BrandsModel

# Register your models here.


@admin.register(BrandsModel)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'id')
    model = BrandsModel
