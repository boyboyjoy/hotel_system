from django.db import models
from database_view.models.hotel_class_model import HotelClassModel
from database_view.models.hotels_chain_model import HotelsChainModel

class HotelModel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotels_chain_id = models.ForeignKey(HotelsChainModel, on_delete=models.CASCADE)
    hotel_class_id = models.ForeignKey(HotelClassModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return 'Hotel'
