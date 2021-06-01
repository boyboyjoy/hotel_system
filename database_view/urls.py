from django.urls import path
from .views import index
from .views import AvailableRooms, MyServices, personal_area, search_hotels

urlpatterns = [
    path('', index, name='index'),
    path('availableRooms/', AvailableRooms.as_view(), name='available_rooms'),
    path('searchRooms/', AvailableRooms.as_view(), name='search_rooms'),
    path('searchHotels/', search_hotels, name='search_hotels'),
    path('services/', AvailableRooms.as_view(), name='services_list'),
    path('myServices/', MyServices.as_view(), name='my_services_list'),
    path('personalArea/', personal_area, name='personal_area')

]
