from django.urls import path
from .views import *

urlpatterns = [
    path('student/<int:pk>', getStudentBookings, name='student-bookings'),
    path('new/showing/<int:pk>', newBooking, name='new-booking'),
    path('<int:pk>/payment', payment, name='payment'),
    path('<int:pk>/cancel', cancelBooking, name='cancel-booking'),
]
