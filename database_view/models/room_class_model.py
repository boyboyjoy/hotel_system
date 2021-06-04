from django.db import models


class RoomClassModel(models.Model):
    room_class_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Классы номеров'
        verbose_name_plural = 'Классы номеров'