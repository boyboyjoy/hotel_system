from django.contrib import admin
from database_view.models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'patronymic', 'function_id')
    list_filter = ('first_name', 'second_name', 'hotel_id', 'function_id')


admin.site.register(BookingModel)
admin.site.register(BookingRequestModel)
admin.site.register(BuildingModel)
admin.site.register(CityModel)
admin.site.register(EmployeeModel, EmployeeAdmin)
admin.site.register(FunctionModel)
admin.site.register(HotelClassModel)
admin.site.register(HotelModel)
admin.site.register(HotelsChainModel)
admin.site.register(ReviewModel)
admin.site.register(RoomClassModel)
admin.site.register(RoomModel)
admin.site.register(ServiceClassModel)
admin.site.register(ServiceModel)
admin.site.register(StreetModel)
admin.site.register(MyUser)


# Register your models here.
