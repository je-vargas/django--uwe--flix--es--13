from django.db import models
from django.urls import reverse
import uuid

class TicketType(models.Model):
    ticket = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.ticket

class Film(models.Model):
    title = models.CharField(max_length=50, null=False)
    age_rating = models.CharField(max_length=20)
    duration = models.CharField(max_length=30)
    film_description = models.CharField(max_length=500, null=False)
    release_date = models.DateField()
    
    #* get_absolute_url needs to be added to every model along with __str__
    def __str__(self):
        return self.title[:50]+ " " + self.age_rating

    #* get_absolute_url - redirects after submitting a from to film detail
    def get_absolute_url(self):
        return reverse("film-detail", args=[str(self.id)])

class CardDetails(models.Model):
    card_number = models.BigIntegerField(null=False)
    expiry_date = models.DateField(null=False)

    def __str__(self):
        r_str = "{0} {1}".format(self.card_number, self.expiry_date)
        return r_str

class Account(models.Model):
    account_title = models.CharField(max_length=50, null=False)
    account_discount = models.BigIntegerField(null=True)
    card_details_id = models.ForeignKey(CardDetails, on_delete=models.PROTECT)

    def __str__(self):
        return self.account_title + " " + self.account_discount

class Booking(models.Model):
    booking_cost = models.IntegerField(null=False)
    number_of_tickets = models.IntegerField(null=False)
    
    def __str__(self):
        r_str = "{0} {1}".format(self.booking_cost, self.number_of_tickets)
        return r_str



class Address(models.Model):
    house_number: models.IntegerField(null=False)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)

class ContactDetails(models.Model):
    landline = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=254)

class LoginAccount(models.Model):
    username = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    createdOn = models.DateTimeField(auto_now=False, auto_now_add=False)
    last_logged_in = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        r_str = "{0} {1} {2}".format(self.username, self.createdOn, self.last_logged_in )
        return r_str

class Representative(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    unique_number = models.UUIDField(default=uuid.uuid4)
    unique_password = models.CharField(max_length=50)
    login_account_id = models.ForeignKey(LoginAccount, on_delete=models.CASCADE)

class Club(models.Model):
    club_name = models.CharField(max_length=100, null=False)
    club_guid = models.UUIDField(default=uuid.uuid4)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact_details_id = models.ForeignKey(ContactDetails, on_delete=models.CASCADE)
    club_rep = models.ForeignKey(Representative, blank=True, on_delete=models.CASCADE)

class LoginTransaction(models.Model):
    date_of_payment = models.DateTimeField(null=False)
    booking_id = models.ForeignKey(Booking, on_delete=models.PROTECT)
    account_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    club_id = models.ForeignKey(Club, on_delete=models.PROTECT)
    
class GuessTransaction(models.Model):
    date_of_payment = models.DateTimeField(null=False)
    booking_id = models.ForeignKey(Booking, on_delete=models.PROTECT)
    card_details_id = models.ForeignKey(CardDetails, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        r_str = "{0} {1} {2}".format(self.booking_id, self.card_details_id, self.date_of_payment)
        return r_str

class Roles(models.Model):
    roles = models.CharField(max_length=50)

class AccountRole(models.Model):
    login_account_id = models.ForeignKey(LoginAccount, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Roles, on_delete=models.PROTECT)

class Showing(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        r_str = "{0} {1} {2}".format(self.film_id, self.time, self.date)
        return r_str

class Screen(models.Model):
    screen_number = models.IntegerField()
    screen_seats_number = models.IntegerField()
    showings_id = models.ManyToManyField(Showing, blank=True)
    
    def __str__(self):
        r_str = "{0} {1} {2}".format(self.screen_number, self.screen_seats_number, self.showings_id )
        return r_str

class BookedTickets(models.Model):
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    ticket_type_id = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    screen_showing_id = models.ForeignKey(Showing, on_delete=models.CASCADE)

    def __str__(self):
        r_str = "{0} {1} {2}".format(self.booking_id, self.ticket_type_id, self.screen_showing_id)
        return r_str

