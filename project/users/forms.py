from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

BACKOFFICE_ROLES = (('cinema manager','Cinema Manager'), ('accounts manager', 'Accounts Manager'))
class RegisterUserForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    role = forms.ChoiceField(choices=BACKOFFICE_ROLES, required=False, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        
class AccountUpdateForm(UserChangeForm):
    
    username = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

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



    


    