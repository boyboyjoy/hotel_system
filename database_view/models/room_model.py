from django.db import models

from database_view.models.hotel_model import HotelModel
from database_view.models.room_class_model import RoomClassModel

class RoomModel(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_class_id = models.ForeignKey(RoomClassModel, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    floor = models.IntegerField(null=False, blank=False)
    is_booked = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return 'Room'

    class Meta:
        verbose_name = 'Номера'
        verbose_name_plural = 'Номера'
