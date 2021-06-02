from django.db import models

from database_view.models.hotel_model import HotelModel
from database_view.models.user_model import UserModel

class BookingRequestModel(models.Model):
    booking_request_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    planned_check_in_date = models.DateField()


    def __str__(self):
        return 'BookingRequest'