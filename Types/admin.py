from django.contrib import admin
from .models import TypesModel
# Register your models here.


@admin.register(TypesModel)
class AdminTypes(admin.ModelAdmin):
    list_display = ('id', 'name', 'resume')
    model = TypesModel    