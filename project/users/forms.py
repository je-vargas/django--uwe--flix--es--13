from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms
from .models import Club

BACKOFFICE_ROLES = (('cinema manager','Cinema Manager'), ('accounts manager', 'Accounts Manager'))
PHONE_REGEX = RegexValidator('^(?:0|\+?44)\s?(?:\d\s?){9,11}$', message='Please enter a valid mobile number starting with +44... or 0... ')

class DateCustomWidget(forms.DateInput):
    input_type = 'date'
class RegisterUserForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    dob = forms.DateField(required=True, widget=DateCustomWidget(attrs={'class':'form-control'}))
    role = forms.ChoiceField(choices=BACKOFFICE_ROLES, required=False, widget=forms.Select(attrs={'class':'form-control'}))
    club = forms.ModelChoiceField(queryset=Club.objects.all(), required=False, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'dob' , 'club' ,'role', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.attrs['class'] = 'form-control'
        self.fields['club'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
class AccountUpdateForm(UserChangeForm):
    
    username = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    dob = forms.DateField(required=True, widget=DateCustomWidget(attrs={'class':'form-control'}))
    club = forms.ModelChoiceField(queryset=Club.objects.all(), required=False, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'dob', 'club' )

    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.attrs['class'] = 'form-control'
        self.fields['club'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class AccountUpdateBackOfficeForm(UserChangeForm):

    username = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    role = forms.ChoiceField(choices=BACKOFFICE_ROLES, required=False, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role')

    def __init__(self, *args, **kwargs):
        super(AccountUpdateBackOfficeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'

class RegisterClubForm(forms.ModelForm):
    name = forms.CharField(max_length=300, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(max_length=15, required=False, validators=[PHONE_REGEX],widget=forms.TextInput(attrs={'class':'form-control'}))
    landline = forms.CharField(max_length=15, required=False, validators=[PHONE_REGEX], widget=forms.TextInput(attrs={'class':'form-control'}))
    house_number = forms.CharField(max_length=300, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    street = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=300, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    postcode = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Club
        fields = ('name', 'email', 'mobile', 'landline', 'house_number', 'street', 'city', 'postcode')

    def __init__(self, *args, **kwargs):
        super(RegisterClubForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['landline'].widget.attrs['class'] = 'form-control'
        self.fields['house_number'].widget.attrs['class'] = 'form-control'
        self.fields['street'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['postcode'].widget.attrs['class'] = 'form-control'


    


    