from django import forms
from database_view.models import MyUser

class UserRegistrationForm(forms.ModelForm):
    password =  forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Пароль ещё раз', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'patronymic')
        labels = {
            'email': 'Email', 'first_name':'Имя', 'last_name':'Фамилия', 'patronymic':'Отчество'
        }

    def clean_password_confirmation(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirmation']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password_confirmation']