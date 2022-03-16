from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # username =forms.CharField(max_length=200, required=True)
    email = forms.EmailField()
    age = forms.IntegerField()
    
    class Meta:
        model = CustomUser
        fields = ('email', 'age',  'username')

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', )