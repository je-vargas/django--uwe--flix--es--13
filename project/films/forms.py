from django import forms 
from django.core.validators import RegexValidator
from .models import *

class DateCustomWidget(forms.DateInput):
    input_type = 'date'

class TimeCustomWidget(forms.TimeInput):
    input_type = 'time'

class NewFilmsForm(forms.ModelForm):
    title = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    age_rating = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    film_description = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
    duration = forms.TimeField(required=True, widget=TimeCustomWidget(format='%H:%M', attrs={'class':'form-control'}))
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
    time_regex = RegexValidator('^([0-1][0-9]|[2][0-3]):([0-5][0-9])$', message='Enter time as HH:MM, e.g. 13:20')

    time = forms.CharField(max_length=50, required=False, validators=[time_regex] ,widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(required=False, widget=DateCustomWidget(attrs={'class':'form-control'}))
    
    class Meta:
        model = Showing
        fields = ('film_id','time', 'date')

    def __init__(self, *args, **kwargs):
        super(NewShowingsForm, self).__init__(*args, **kwargs)
        self.fields['film_id'].widget.attrs['class'] = 'form-control'
        self.fields['time'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'

class UpdateShowingForm(NewShowingsForm): pass

class NewScreenForm(forms.ModelForm):

    screen_number = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))
    screen_seats_number = forms.IntegerField( required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Screen
        fields = ('screen_number', 'screen_seats_number', 'showings_id')

    def __init__(self, *args, **kwargs):
        super(NewScreenForm, self).__init__(*args, **kwargs)
        self.fields['screen_number'].widget.attrs['class'] = 'form-control'
        self.fields['screen_seats_number'].widget.attrs['class'] = 'form-control'
        self.fields['showings_id'].widget.attrs['class'] = 'form-control'

    def clean_screen_number(self):
        screen_number = self.cleaned_data['screen_number']
        if Screen.objects.filter(screen_number=screen_number).exists():
            raise ValidationError("Screen already exists")
        return screen_number


class UpdateScreenForm(NewScreenForm): pass