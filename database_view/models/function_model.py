from django.db import models


class FunctionModel(models.Model):
    function_id = models.AutoField(primary_key=True)
    function_name = models.CharField(max_length=20, null=False, blank=False)
    salary = models.FloatField(null=False, blank=False)
