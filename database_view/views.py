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
from database_view.models.review_model import ReviewModel
from database_view.models.booking_request_model import BookingRequestModel
from database_view.forms import HotelsSearchForm, RoomsSearchForm, ReviewForm, LoginForm, UserRegistrationForm, ServiceRequestForm
from database_view.forms import BookingRequestForm

import io
from django.http import FileResponse


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

def get_available_rooms(request):
    rooms = RoomModel.objects.filter(is_booked=False)
    return render(request, 'available_rooms/available_roms.html', {'rooms':rooms})

class MyServices(ListView):
    model = ServiceModel
    template_name = 'my_services/my_services_list.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServiceModel.objects.filter(user_id=self.request.user.id)

def personal_area(request):
    if not request.user.is_authenticated:
        return redirect('login')

    booking_request = list(BookingModel.objects.filter(user_id=request.user.id))


    return render(request, 'personal_area/personal_area_list.html', {'user': request.user,
                                                                     'rooms': booking_request})

def search_hotels(request):
    if not request.user.is_authenticated:
        redirect('login')

    if request.method == 'POST':
        form = HotelsSearchForm(request.POST)
        form.is_valid()
        hotels = HotelModel.objects.filter(hotel_class_id=form.cleaned_data['hotel_class'],
                                           hotels_chain_id=form.cleaned_data['hotel_chain'])
        return render(request, 'search_hotels/search_hotels.html', {'form': form, 'hotels': hotels})
    form = HotelsSearchForm()
    return render(request, 'search_hotels/search_hotels.html', {'form' : form })

def search_rooms(request):
    if not request.user.is_authenticated:
        return request('login')

    if request.method == 'POST':
        form = RoomsSearchForm(request.POST)
        form.is_valid()
        rooms = RoomModel.objects.filter(room_class_id=form.cleaned_data['room_class'])
        new_rooms = []
        for room in rooms:
            if room.hotel_id.hotel_class_id == form.cleaned_data['hotel_class'] \
                and room.hotel_id.hotels_chain_id == form.cleaned_data['hotel_chain']:
                new_rooms.append(room)

        return render(request, 'search_rooms/search_rooms.html', {'form':form, 'rooms':new_rooms})
    form = RoomsSearchForm()
    return render(request, 'search_rooms/search_rooms.html', {'form' : form })

def make_review(request, hotel):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.is_valid()
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        hotel_inst = HotelModel.objects.get(hotel_id=hotel)
        ReviewModel.objects.create(title=title, description=description, hotel_id=hotel_inst, user_id=request.user, mark=5)
        return redirect('index')
    form = ReviewForm()
    return render(request, 'review/make_review.html', {'form' : form, 'hotel_id': hotel})

def get_review(request, hotel_id):
    if not request.user.is_authenticated:
        return redirect('login')

    reviews = ReviewModel.objects.filter(hotel_id=hotel_id)
    return render(request, 'review/review_list.html', {'reviews':reviews, 'hotel_name': HotelModel.objects.get(hotel_id=hotel_id).name})

def make_service_request(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
    form = ServiceRequestForm()
    return render(request, 'services/service_request.html', {'form' : form })

def get_services(request):
    if not request.user.is_authenticated:
        return redirect('login')

    services = ServiceClassModel.objects.all()

    return render(request, 'services/services_list.html', {'services': services})

def get_user_services(request):
    services = ServiceModel.objects.all()

    return render(request, 'my_services/my_services_list.html', {'services': services})

def make_booking(request, room_id):
    if not request.user.is_authenticated:
        return redirect('login')
    room_inst = RoomModel.objects.get(room_id=room_id)
    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        form.is_valid()
        BookingRequestModel.objects.create(user_id=request.user, room_id=room_inst,
                                           planned_check_in_date=form.cleaned_data['check_in_date'],
                                           planned_check_out_date=form.cleaned_data['check_out_date'])
        return redirect('booking_requests')
    form = BookingRequestForm()
    return render(request, 'booking_requests/make_booking_request.html', {'form': form, 'room_id':room_id})

def get_booking_requests(request):
    if not request.user.is_authenticated:
        return request(request, 'login')
    requests = BookingRequestModel.objects.filter(user_id=request.user)

    return render(request, 'booking_requests/booking_request.html', {'requests': requests})

def remove_booking_request(request,  booking_id):
    if not request.user.is_authenticated:
        return request(request, 'login')
    BookingRequestModel.objects.get(booking_request_id=booking_id).delete()
    return redirect('booking_requests')

