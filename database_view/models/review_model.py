from django.db import models
from database_view.models.hotel_model import HotelModel
from database_view.models.user_model import UserModel

class ReviewModel(models.Model):
    review_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=20, null=False, blank=False)
    mark = models.FloatField(null=False, blank=False)
