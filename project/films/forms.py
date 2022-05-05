from django import forms 
from django.core.validators import RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError

from .models import *

TIME_REGEX = RegexValidator('^([0-1][0-9]|[2][0-3]):([0-5][0-9])$', message='Enter time as HH:MM, e.g. 13:20')

class DateCustomWidget(forms.DateInput):
    input_type = 'date'

class TimeCustomWidget(forms.TimeInput):
    input_type = 'time'

class NewFilmsForm(forms.ModelForm):
    FILM_AGE = (('U','U'), ('PG', 'PG'), ('12A', '12A'), ('12', '12'), ('15', '15'), ('18', '18'), ('R18', 'R18'))
    
    title = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    age_rating = forms.ChoiceField(choices=FILM_AGE, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    film_description = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
    duration = forms.IntegerField(required=True, validators=[MinValueValidator(0)],  widget=forms.NumberInput(attrs={'class':'form-control'}))
    release_date = forms.DateField(required=True, widget=DateCustomWidget(attrs={'class':'form-control'}))

    class Meta:
        model = Film
        fields = ('title', 'film_description', 'age_rating', 'duration', 'release_date')

    def __init__(self, *args, **kwargs):
        super(NewFilmsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['age_rating'].widget.attrs['class'] = 'form-control'
        self.fields['duration'].widget.attrs['class'] = 'form-control'
        self.fields['film_description'].widget.attrs['class'] = 'form-control'
        self.fields['release_date'].widget.attrs['class'] = 'form-control'


class UpdateFilmForm(NewFilmsForm): pass

class NewShowingsForm(forms.ModelForm):
    
    time = forms.CharField(max_length=50, required=False, validators=[TIME_REGEX] ,widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(required=False, widget=DateCustomWidget(attrs={'class':'form-control'}))
    screen = forms.ModelChoiceField(queryset=Screen.objects.all())
    
    class Meta:
        model = Showing
        fields = ('film', 'screen','time', 'date')

    def __init__(self, *args, **kwargs):
        super(NewShowingsForm, self).__init__(*args, **kwargs)
        self.fields['film'].widget.attrs['class'] = 'form-control'
        self.fields['time'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'

class UpdateShowingForm(NewShowingsForm): pass

class NewScreenForm(forms.ModelForm):

    number = forms.IntegerField(required=True, validators=[MinValueValidator(1)], widget=forms.NumberInput(attrs={'class':'form-control'}))
    capacity = forms.IntegerField( required=True, validators=[MinValueValidator(1)], widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Screen
        fields = ('number', 'capacity')

    def __init__(self, *args, **kwargs):
        super(NewScreenForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs['class'] = 'form-control'
        self.fields['capacity'].widget.attrs['class'] = 'form-control'

    def clean(self):
        if self.cleaned_data == {}: return
        number = self.cleaned_data['number']

        if Screen.objects.filter(number=number).exists(): 
            raise ValidationError(('Screen already exists'), code='invalid')
        return

    


class UpdateScreenForm(NewScreenForm): pass