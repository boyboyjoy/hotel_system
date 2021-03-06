from django.db import models
from .my_user import MyUser

from database_view.models.hotel_model import HotelModel


class ReviewModel(models.Model):
    review_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=20, null=False, blank=False)
    mark = models.FloatField(null=False, blank=False)

    def __str__(self):
        return 'Review'


    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'