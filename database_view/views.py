from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from database_view.models.room_model import RoomModel
from database_view.models.service_model import ServiceModel
from database_view.forms import HotelsSearchForm, RoomsSearchForm

def index(request):
    return render(request, 'menu.html')


class AvailableRooms(ListView):
    model = RoomModel
    template_name = 'available_rooms/available_roms.html'
    queryset = RoomModel.objects.all()

class MyServices(ListView):
    model = ServiceModel
    template_name = 'my_services/my_services_list.html'
    queryset = ServiceModel.objects.all()

def personal_area(request):
    return render(request, 'personal_area/personal_area_list.html')

def search_hotels(request):
    if request.method == 'GET':
        form = HotelsSearchForm(request.GET)
    form = HotelsSearchForm()
    return render(request, 'search_hotels/search_hotels.html', {'form' : form })

def search_rooms(request):
    if request.method == 'GET':
        form = RoomsSearchForm(request.GET)
    form = RoomsSearchForm()
    return render(request, 'search_rooms/search_rooms.html', {'form' : form })

