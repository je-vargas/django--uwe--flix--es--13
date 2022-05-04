from django.urls import path
from .views import *

urlpatterns = [
    path('new', newBooking, name='new-booking')
]
