from django.urls import path
from .views import *

urlpatterns = [
    path('', getBookings, name='all-bookings'),
    path('cancelled/', getCancelledBookings, name='all-cancelled-bookings'),
    path('student/<int:pk>', getStudentBookings, name='student-bookings'),
    path('club/<int:pk>', getClubBookings, name='club-bookings'),
    path('new/showing/<int:pk>', newBooking, name='new-booking'),
    path('<int:pk>/payment', payment, name='payment'),
    path('<int:pk>/cancel', cancelBooking, name='cancel-booking'),
    path('<int:pk>cancelled/approve', approveBookingCancel, name='approve-booking-cancelled'),
]
