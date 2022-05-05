from django import forms 
from django.core.validators import RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError

from .models import *
class NewBookingForm(forms.ModelForm):
    # TICKET_TYPE = ['student', 'child', 'adult']
    # ticket = forms.ChoiceField(choices=TICKET_TYPE, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    # booking_cost = forms.FloatField(required=True, widget=forms.Select(attrs={'class':'form-control'}))
    # number_of_tickets = forms.IntegerField(required=True, validators=[MinValueValidator(0)], widget=forms.Textarea(attrs={'class':'form-control'}))
    # showing = forms.Forei

    class Meta:
        model = Booking
        fields = ('ticket', 'number_of_tickets', 'showing', 'booking_cost')

    def __init__(self, *args, **kwargs):
        super(NewBookingForm, self).__init__(*args, **kwargs)
        self.fields['ticket'].widget.attrs['class'] = 'form-control'
        self.fields['number_of_tickets'].widget.attrs['class'] = 'form-control'
        self.fields['showing'].widget.attrs['class'] = 'form-control'
        self.fields['booking_cost'].widget.attrs['class'] = 'form-control'