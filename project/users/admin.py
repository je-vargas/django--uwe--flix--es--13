from django.contrib import admin
from .models import (
    Club,
    ClubUsers
    )

admin.site.register(Club)
admin.site.register(ClubUsers)