from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from database_view.models.room_model import RoomModel

def index(request):
    return render(request, 'menu.html')


class AvailableRooms(ListView):
    model = RoomModel
    template_name = 'available_rooms/available_roms.html'
    queryset = RoomModel.objects.all()

