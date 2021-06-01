from django.db import models


class HotelsChainModel(models.Model):
    hotels_chain_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)
