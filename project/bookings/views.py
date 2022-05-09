from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import Group, User
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict

from decorators import allowed_users
from films.models import Film, Showing
from .models import *
from .forms import *
from access import * 

import datetime

def bookingDiscount(discount, booking_total):
    rate = 1-(discount/100)
    return booking_total*rate

def getBookings(request, pk): 
    return HttpResponse(f'needs implementing user: {pk}')

@allowed_users(['club reps', 'student'])
def newBooking(request, pk):

    showing_obj = get_object_or_404(Showing, pk=pk)

    form = NewBookingForm(request.POST or None)
    
    if request.method == "POST":
        
        if form.is_valid():

            booking_obj = form.save(commit=False)
            showing_obj.capacity = showing_obj.capacity - booking_obj.number_of_tickets
            showing_obj.save()

            booking_obj.showing = showing_obj
            booking_obj.cost = showing_obj.price * booking_obj.number_of_tickets
            booking_obj.save()
            
            return redirect('payment', pk=booking_obj.pk)
        else:
            return render(request, 'bookings/new_booking.html', {
                "form":form,
                'showing':showing_obj,
                "film":request.POST.get('form-0-film-id'),
                "time":request.POST.get('form-1-time'),
                "date":request.POST.get('form-2-date')
                })
    else:
        print(request)
        form = NewBookingForm()
        return render(request, 'bookings/new_booking.html', {
            'showing':showing_obj,
            'form':form
            })

def payment(request, pk):
    
    user_role = get_user_groups(request)
    user_id = request.user.pk
    
    #* try get object if not delete booking made otherwise we have inacessible data
    booking_obj = get_object_or_404(Booking, pk=pk)
    account_obj = get_object_or_404(Account, user=user_id)

    discount = account_obj.account_discount
    booking_total = booking_obj.cost
    
    booking_with_discount = 0

    #* check if discount has already been applied to this booking
    if booking_obj.is_discount_applied is not True and 'club rep' in user_role :
        booking_with_discount = bookingDiscount(discount, booking_total)
        booking_obj.is_discount_applied = True
        booking_obj.discount_cost = booking_with_discount
        booking_obj.save()

    form = PaymentForm(request.POST or None)
    
    if request.method == "POST":
        
        if form.is_valid():

            card_obj = form.save()

            transaction_obj = LoginTransaction(
                date_of_payment=datetime.datetime.now(), 
                booking=booking_obj,
                account = account_obj,
                discount_at_purchase= account_obj.account_discount, 
                card_number=card_obj.card_number
                )
            transaction_obj.save()
            
            return redirect('bookings', user_id)
        else:
            return render(request, 'bookings/payment.html', {
                "discount": account_obj.account_discount,
                "booking_total": booking_total,
                "booking_with_discount": booking_with_discount,
                "form":form,
                "card_number":request.POST.get('form-0-expiry-number'),
                "expiry_date":request.POST.get('form-1-expiry-date'),
                })
        
    else:
        form = PaymentForm()
        return render(request, 'bookings/payment.html', {
            "discount": account_obj.account_discount,
            "booking_total": booking_total,
            "booking_with_discount": booking_with_discount,
            'form':form
            })