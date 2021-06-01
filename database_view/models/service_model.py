from django.db import models
from database_view.models.employee_model import EmployeeModel
from database_view.models.service_class_model import ServiceClassModel
from database_view.models.user_model import UserModel

class ServiceModel(models.Model):
    service_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    service_class_id = models.ForeignKey(ServiceClassModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    execution_date = models.DateTimeField()
