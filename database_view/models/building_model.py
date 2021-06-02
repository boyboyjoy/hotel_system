from django.db import models


class BuildingModel(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_number = models.IntegerField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.building_number