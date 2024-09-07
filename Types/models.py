from django.db import models

# Create your models here.


class TypesModel(models.Model):
    name = models.CharField(max_length=50)
    resume = models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.name
