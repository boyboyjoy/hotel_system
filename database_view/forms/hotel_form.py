from django.forms import Form, CharField, DateTimeField, DateTimeInput, ModelChoiceField
from database_view.models import HotelModel, HotelClassModel, HotelsChainModel, CityModel

class HotelsSearchForm(Form):
    hotel_class = ModelChoiceField(label='Класс гостиницы', queryset=HotelClassModel.objects.all())
    hotel_chain = ModelChoiceField(label='Сеть гостиниц', queryset=HotelsChainModel.objects.all())
    city = ModelChoiceField(label='Город', queryset=CityModel.objects.all())
