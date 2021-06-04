from django.db import models
from database_view.models.city_model import CityModel

class StreetModel(models.Model):
    street_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    city_id = models.ForeignKey(CityModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улицы'
        verbose_name_plural = 'Улицы'