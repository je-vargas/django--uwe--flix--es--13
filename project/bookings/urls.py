from django.urls import path
from .views import *

urlpatterns = [
    path('user/<int:pk>', getBookings, name='bookings'),
    path('new/showing/<int:pk>', newBooking, name='new-booking'),
    path('<int:pk>/payment', payment, name='payment'),
]
