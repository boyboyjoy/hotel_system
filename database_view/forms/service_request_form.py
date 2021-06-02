from django.forms import ModelForm,Form, CharField, DateTimeField, DateTimeInput, ModelChoiceField
from database_view.models import HotelModel, HotelClassModel, HotelsChainModel, CityModel
from database_view.models import ServiceModel

class ServiceRequestForm(ModelForm):
    #date = DateTimeField(label='Выберите дату для услуги', widget=DateTimeInput(attrs={'time':'datetime-local'}))
    class Meta:
        model = ServiceModel
        fields = ['execution_date']
        labels = {'execution_date': 'Дата Услуги'}
        widgets = {
            'execution_date': DateTimeInput(
                attrs={'type': 'datetime-local'}),
        }
