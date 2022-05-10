from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.contrib import messages

from decorators import allowed_users
from films.models import Film, Showing
from users.models import ClubUsers
from .models import *
from .forms import *
from access import * 

import datetime

def bookingDiscount(discount, booking_total):
    rate = 1-(discount/100)
    return booking_total*rate

def getBookingForm(request):
    if request.user.groups.exists():
        user_role = get_user_groups(request)
    
        if 'club rep' in user_role : return NewBookingClubRepForm(request.POST or None)
    
    return NewBookingForm(request.POST or None) 

def getBookingRedirect(request):
    if request.user.groups.exists():
        user_role = get_user_groups(request)
    
        if 'club rep' in user_role : return 'club-bookings'
    
    return 'student-bookings'



#* -------------- VIEWS -----------------
@allowed_users(['cinema manager', 'staff'])
def getBookings(request): 

    all_transaction = LoginTransaction.objects.all()

    return render(request,'bookings/bookings_all.html', {
            "transactions": all_transaction,
        })

@allowed_users(['cinema manager', 'staff'])
def getCancelledBookings(request): 

    all_transaction = LoginTransaction.objects.filter(booking__cancelled = True)

    return render(request,'bookings/bookings_all.html', {
            "transactions": all_transaction,
        })

@allowed_users(['student'])
def getStudentBookings(request, pk): 

    account_table = get_object_or_404(Account, user=pk)
    all_transaction = LoginTransaction.objects.all().filter(account=account_table.pk)

    return render(request,'bookings/bookings_all.html', {
            "transactions": all_transaction,
            "user": account_table.user,
            "account_name":account_table.account_title
        })

@allowed_users(['club rep'])
def getClubBookings(request, pk): 

    all_transaction = LoginTransaction.objects.none()
    account_title = None

    user_table = get_object_or_404(User, pk=pk)
    club_link = get_object_or_404(ClubUsers, user=pk)
    account_table = Account.objects.filter(account_title = club_link.club.name)
    for user_in_account in account_table: 
        account_title = user_in_account.account_title
        all_transaction = all_transaction.union(LoginTransaction.objects.all().filter(account=user_in_account.id))
    
    

    return render(request,'bookings/bookings_all.html', {
            "transactions": all_transaction,
            "user": user_table,
            "account_name":account_title
        })

@allowed_users(['club rep', 'student'])
def newBooking(request, pk):

    showing_obj = get_object_or_404(Showing, pk=pk)
    form = getBookingForm(request)
    
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
        form = getBookingForm(request)
        return render(request, 'bookings/new_booking.html', {
            'showing':showing_obj,
            'form':form
            })

def payment(request, pk):
    
    booking_redirect = getBookingRedirect(request)
    user_role = get_user_groups(request)
    user_id = request.user.pk
    
    #* try get object if not delete booking made otherwise we have inacessible data
    booking_obj = get_object_or_404(Booking, pk=pk)
    account_obj = get_object_or_404(Account, user=user_id)

    discount = account_obj.account_discount
    booking_total = booking_obj.cost
    
    booking_with_discount = booking_obj.discount_cost

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
            
            return redirect(booking_redirect, user_id)
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
            "discount": discount,
            "booking_total": booking_total,
            "booking_with_discount": booking_with_discount,
            'form':form
            })

def cancelBooking(request, pk):
    booking_redirect = getBookingRedirect(request) 

    booking_table_obj = get_object_or_404(Booking, pk=pk)
    user_table_obj = get_object_or_404(User, pk=request.user.pk)

    booking_table_obj.cancelled = True
    booking_table_obj.save()

    cancelled_booking_table_obj = CancelledBookings(
        date=datetime.datetime.now(),
        booking=booking_table_obj, 
        user=user_table_obj, 
        
    )
    cancelled_booking_table_obj.save()
    messages.success(request, "Cancelled booking request successfull, will be removed once approved")
    return redirect(booking_redirect, user_table_obj.pk)

def approveBookingCancel(request, pk):
    booking_redirect = getBookingRedirect(request) 

    booking_table_obj = get_object_or_404(Booking, pk=pk)
    cancelled_booking_table_obj = get_object_or_404(CancelledBookings, booking=booking_table_obj.pk)
    cancelled_booking_table_obj.approved = True
    cancelled_booking_table_obj.save()

    messages.success(request, "Booking Cancelled")
    return redirect('all-cancelled-bookings')