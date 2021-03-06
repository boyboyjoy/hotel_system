from django.db import models
from .my_user import MyUser
import datetime

from database_view.models.hotel_model import HotelModel
from database_view.models.room_model import RoomModel

class BookingRequestModel(models.Model):
    booking_request_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    room_id = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    planned_check_in_date = models.DateField()
    planned_check_out_date = models.DateField(default=datetime.date.today())
    status = models.CharField(null=False, default='В обработке', max_length=20)


    def __str__(self):
        return 'BookingRequest'

    class Meta:
        verbose_name = 'Заявки на бронирование'
        verbose_name_plural = 'Заявки на бронирование'