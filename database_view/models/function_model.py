from django.db import models


class FunctionModel(models.Model):
    function_id = models.AutoField(primary_key=True)
    function_name = models.CharField(max_length=20, null=False, blank=False)
    salary = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.function_name

    class Meta:
        verbose_name = 'Должности'
        verbose_name_plural = 'Должности'