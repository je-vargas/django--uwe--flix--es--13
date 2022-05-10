from django import forms 
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from .models import *

class DateCustomWidget(forms.DateInput):
    input_type = 'date'

class NewBookingForm(forms.ModelForm):
    number_of_tickets = forms.IntegerField(required=True, validators=[MinValueValidator(1, message="Minimum booking required is 1 ticket"), MaxValueValidator(1, message="Maximum booking permited is 1 ticket"
    )], widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Booking
        fields = ('ticket', 'number_of_tickets')

    def __init__(self, *args, **kwargs):
        super(NewBookingForm, self).__init__(*args, **kwargs)
        self.fields['ticket'].widget.attrs['class'] = 'form-control'
        self.fields['number_of_tickets'].widget.attrs['class'] = 'form-control'

class NewBookingClubRepForm(NewBookingForm):
    number_of_tickets = forms.IntegerField(required=True, validators=[MinValueValidator(1, message="Minimum booking required is 1 ticket"), MaxValueValidator(10, message="Maximum booking permited is 10 tickets"
    )], widget=forms.NumberInput(attrs={'class':'form-control'}))

class PaymentForm(forms.ModelForm):
    
    valid_card = RegexValidator("[0-9]{16}", message='Invalid card number, must be 16 digits long')

    card_number = forms.CharField(required=True, validators=[valid_card], widget=forms.TextInput(attrs={'class':'form-control'}))
    expiry_date = forms.DateField(required=True, widget=DateCustomWidget(attrs={'class':'form-control'}))


    class Meta:
        model = CardDetails
        fields = ('card_number', 'expiry_date')

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['card_number'].widget.attrs['class'] = 'form-control'
        self.fields['expiry_date'].widget.attrs['class'] = 'form-control'

    
