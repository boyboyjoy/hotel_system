from django.db import models
from database_view.models.hotel_model import HotelModel
from database_view.models.function_model import FunctionModel


class EmployeeModel(models.Model):
    employee_id = models.AutoField(primary_key=True)
    function_id = models.ForeignKey(FunctionModel, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    second_name = models.CharField(max_length=20, null=False, blank=False)
    patronymic = models.CharField(max_length=20, null=False, blank=False)


    def __str__(self):
        return self.second_name + ' ' + self.first_name + ' ' + self.patronymic + ' ' + self.function_id.function_name

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'