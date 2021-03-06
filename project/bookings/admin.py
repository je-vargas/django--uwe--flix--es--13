from django.contrib import admin
from .models import (
    TicketType, 
    CardDetails,
    Account,
    Booking,
    LoginTransaction,
    GuessTransaction 
    )

admin.site.register(TicketType)
admin.site.register(CardDetails)
admin.site.register(Account)
admin.site.register(Booking)
admin.site.register(LoginTransaction)
admin.site.register(GuessTransaction)
