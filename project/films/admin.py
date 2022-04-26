from django.contrib import admin
from .models import (
    LoginAccount, 
    Film, 
    Showing, 
    Screen, 
    TicketType,
    BookedTickets, 
    Booking, 
    GuessTransaction,
    CardDetails
    )

admin.site.register(LoginAccount)
admin.site.register(Film)
admin.site.register(Showing)
admin.site.register(Screen)
admin.site.register(TicketType)
admin.site.register(BookedTickets)
admin.site.register(Booking)
admin.site.register(GuessTransaction)
admin.site.register(CardDetails)