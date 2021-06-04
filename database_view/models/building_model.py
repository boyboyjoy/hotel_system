from django.db import models
from .street_model import StreetModel


class BuildingModel(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_number = models.IntegerField(max_length=20, null=False, blank=False)
    street_id = models.ForeignKey(StreetModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.building_number)

    class Meta:
        verbose_name = 'Здания'
        verbose_name_plural = 'Здания'