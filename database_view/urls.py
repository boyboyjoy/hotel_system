from django.urls import path
from .views import index
from .views import get_available_rooms, \
    MyServices, \
    personal_area,\
    search_hotels, \
    search_rooms, \
    make_review, \
    get_services, \
    user_login, \
    get_user_services, \
    user_registration, logout_view, make_booking, make_service_request, get_review, get_booking_requests, remove_booking_request, download_pdf

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_registration, name='register'),
    path('logout/', logout_view, name='logout'),
    path('', index, name='index'),
    path('availableRooms/', get_available_rooms, name='available_rooms'),
    path('searchRooms/', search_rooms, name='search_rooms'),
    path('searchHotels/', search_hotels, name='search_hotels'),
    path('services/', get_services, name='services_list'),
    path('myServices/', get_user_services, name='my_services_list'),
    path('personalArea/', personal_area, name='personal_area'),
    path('makeReview/<int:hotel>', make_review, name='make_review'),
    path('bookingRequest/<int:room_id>', make_booking, name='booking_request'),
    path('serviceRequest', make_service_request, name='make_service_request'),
    path('getReviews/<int:hotel_id>', get_review, name='get_review'),
    path('getBookingRequests', get_booking_requests, name='booking_requests'),
    path('removeBookingRequest/<int:booking_id>', remove_booking_request, name='remove_booking_request'),
    path('downloafPDF/<int:room_id>', download_pdf, name='download_pdf')
]
