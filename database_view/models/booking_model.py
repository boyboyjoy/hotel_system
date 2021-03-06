from django.db import models
from .my_user import MyUser

from database_view.models.hotel_model import HotelModel
from database_view.models.room_model import RoomModel

class BookingModel(models.Model):
    booking_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    check_in_date = models.DateField(null=False, blank=False)
    check_out_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return

    class Meta:
        verbose_name = 'Постояльцы'
        verbose_name_plural = 'Постояльцы'