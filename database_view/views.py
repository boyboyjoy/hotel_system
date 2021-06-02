from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from database_view.models.hotel_model import HotelModel
from database_view.models.booking_model import BookingModel
from database_view.models.room_model import RoomModel
from database_view.models.service_model import ServiceModel, ServiceClassModel
from database_view.forms import HotelsSearchForm, RoomsSearchForm, ReviewForm, LoginForm, UserRegistrationForm


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'menu.html')

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('login')


def user_registration(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('index')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Аккаунт отключен')
            else:
                return HttpResponse('Неправильные почта или пароль')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

class AvailableRooms(ListView):
    model = RoomModel
    template_name = 'available_rooms/available_roms.html'
    queryset = RoomModel.objects.all()

class MyServices(ListView):
    model = ServiceModel
    template_name = 'my_services/my_services_list.html'
    queryset = ServiceModel.objects.all()

def personal_area(request):
    if not request.user.is_authenticated:
        return redirect('login')
    booking_request = list(BookingModel.objects.filter(user_id=request.user.id))


    return render(request, 'personal_area/personal_area_list.html', {'user': request.user,
                                                                     'rooms': booking_request})

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

def make_review(request, hotel):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
    form = ReviewForm()
    return render(request, 'review/make_review.html', {'form' : form })

def get_services(request):
    services = ServiceClassModel.objects.all()

    return render(request, 'services/services_list.html', {'services': services})

def get_user_services(request):
    services = ServiceModel.objects.all()

    return render(request, 'my_services/my_services_list.html', {'services': services})

def make_booking(request):
    return None

