from django.forms import Form, CharField, DateTimeField, DateTimeInput, ModelChoiceField, Textarea, ChoiceField
from database_view.models import HotelModel, HotelClassModel, HotelsChainModel, CityModel, RoomClassModel


MARK_CHOICES =(
    (1.0, '1'),
    (2.0, '2'),
    (3.0, '3'),
    (4.0, '4'),
    (5.0, '5'),
)

class ReviewForm(Form):
    title = CharField(label='Заголовок', max_length=20)
    description = CharField(label='Описание', max_length=100, widget=Textarea)
    mark = ChoiceField(choices=MARK_CHOICES)

