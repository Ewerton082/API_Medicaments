from django.db import models

# Create your models here.


class BrandsModel(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name
