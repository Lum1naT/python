from django import forms

CZECH = 'CZE'
SLOVAKIA = 'SVK'
GERMANY = 'GER'
AUSTRIA = 'AUS'

COUNTRY_CHOICES = [
    (CZECH, 'Czech'),
    (SLOVAKIA, 'Slovakia'),
    (GERMANY, 'Germany'),
    (AUSTRIA, 'Austria'),
]

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.EmailField(label='Your Email Address', max_length=200)
    phone_number = forms.IntegerField(label='Your Phone Number')
    country = forms.ChoiceField(choices = COUNTRY_CHOICES)
