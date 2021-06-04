from django.db import models


class CityModel(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'