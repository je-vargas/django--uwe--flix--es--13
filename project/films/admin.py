from django.contrib import admin
from .models import (
    Film, 
    Screen,
    Showing, 
    )

admin.site.register(Film)
admin.site.register(Screen)
admin.site.register(Showing)
