from django.db import models


class HotelClassModel(models.Model):
    hotel_class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)


    def __str__(self):
        return self.name