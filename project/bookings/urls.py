from django.urls import path
from .views import *

urlpatterns = [
    path('', getBookings, name='bookings'),
    path('new', newBooking, name='new-booking'),
]
