from django.forms import Form, CharField, DateTimeField, DateTimeInput, ModelChoiceField
from database_view.models import HotelModel, HotelClassModel, HotelsChainModel, CityModel

class ServiceRequestForm(Form):
    date = DateTimeField(label='Выберите дату для услуги', widget=DateTimeInput)
