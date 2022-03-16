from django.contrib import admin
from .models import Film, Showing, LoginAccount

admin.site.register(Film)
admin.site.register(Showing)
admin.site.register(LoginAccount)