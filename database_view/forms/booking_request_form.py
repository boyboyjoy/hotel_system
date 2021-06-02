from django.forms import Form, CharField, DateTimeField, DateTimeInput, ModelChoiceField
from database_view.models import HotelModel, HotelClassModel, HotelsChainModel, CityModel

class BookingRequestForm(Form):
    check_in_date = DateTimeField(label='Дата заселения', widget=DateTimeInput)
    check_out_date = DateTimeField(label='Дата выселения', widget=DateTimeInput)
