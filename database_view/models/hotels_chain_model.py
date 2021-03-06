from django.db import models


class HotelsChainModel(models.Model):
    hotels_chain_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Сети гостиниц'
        verbose_name_plural = 'Сети гостиниц'