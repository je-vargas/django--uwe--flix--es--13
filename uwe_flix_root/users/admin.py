from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreation, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)