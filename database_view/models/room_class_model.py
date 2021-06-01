from django.db import models


class RoomClassModel(models.Model):
    room_class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

