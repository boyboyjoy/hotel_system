from django.forms import Form, CharField, DateTimeField, DateTimeInput, ModelChoiceField, Textarea
from database_view.models import HotelModel, HotelClassModel, HotelsChainModel, CityModel, RoomClassModel

class ReviewForm(Form):
    title = CharField(label='Заголовок', max_length=20)
    description = CharField(label='Описание', max_length=100, widget=Textarea)

