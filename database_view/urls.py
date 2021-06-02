from django.urls import path
from .views import index
from .views import AvailableRooms, MyServices, personal_area, search_hotels, search_rooms, make_review, get_services

urlpatterns = [
    path('', index, name='index'),
    path('availableRooms/', AvailableRooms.as_view(), name='available_rooms'),
    path('searchRooms/', search_rooms, name='search_rooms'),
    path('searchHotels/', search_hotels, name='search_hotels'),
    path('services/', get_services, name='services_list'),
    path('myServices/', MyServices.as_view(), name='my_services_list'),
    path('personalArea/', personal_area, name='personal_area'),
    path('makeReview/', make_review, name='make_review')

]
