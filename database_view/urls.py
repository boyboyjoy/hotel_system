from django.urls import path
from .views import index
from .views import AvailableRooms

urlpatterns = [
    path('', index, name='index'),
    path('availableRooms/', AvailableRooms.as_view(), name='available_rooms'),
    path('searchRooms/', AvailableRooms.as_view(), name='search_rooms'),
    path('searchHotels/', AvailableRooms.as_view(), name='search_hotels'),
    path('services/', AvailableRooms.as_view(), name='services_list'),
    path('myServices/', AvailableRooms.as_view(), name='my_services_list'),
    path('personalArea/', AvailableRooms.as_view(), name='personal_area')

]
