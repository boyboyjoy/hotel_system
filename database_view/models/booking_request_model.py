from django.db import models
from django.contrib.auth.models import User

from database_view.models.hotel_model import HotelModel

class BookingRequestModel(models.Model):
    booking_request_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    planned_check_in_date = models.DateField()


    def __str__(self):
        return 'BookingRequest'