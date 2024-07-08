from django.db import models
from drf_spectacular.utils import extend_schema 
import json


class Regions(models.Model):
    region_name = models.CharField(max_length=255)
    boundary = models.JSONField()
    
    def get_boundary_list(self):
        return json.loads(self.boundary)


    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = 'Регионы'

    def __str__(self) -> str:
        return self.region_name
    

extend_schema(tags=['Локации'])
class Locations(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = 'Локации'

    def __str__(self) -> str:
        return self.name