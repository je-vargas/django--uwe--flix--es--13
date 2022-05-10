from django.db import models
from django.contrib.auth.models import User

class TicketType(models.Model):
    ticket = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.ticket

class CardDetails(models.Model):
    card_number = models.CharField(max_length=19, null=False)
    expiry_date = models.DateField(null=False)

    def __str__(self):
        r_str = "{0} {1}".format(self.card_number, self.expiry_date)
        return r_str


class Account(models.Model):
    account_title = models.CharField(max_length=50, null=False)
    account_discount = models.FloatField(null=False, default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    card_details = models.ForeignKey(CardDetails, on_delete=models.PROTECT, null=True)

    def __str__(self):
        r_str = "{0} {1}".format(self.account_title, self.account_discount, )
        return r_str

class Booking(models.Model):
    ticket = models.ForeignKey(TicketType, on_delete=models.PROTECT)
    number_of_tickets = models.IntegerField(null=False)
    cost = models.IntegerField(null=False)
    discount_cost = models.IntegerField(null=False, default=0)
    showing = models.ForeignKey('films.Showing', on_delete=models.PROTECT)
    is_discount_applied = models.BooleanField(null=True, default=False)
    
    def __str__(self):
        r_str = "{0} {1} {2} {3}".format(self.cost, self.number_of_tickets, self.ticket, self.showing)
        return r_str

class LoginTransaction(models.Model):
    date_of_payment = models.DateTimeField(null=False)
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    discount_at_purchase = models.FloatField()
    card_number = models.CharField(null=False, max_length=19)

    def __str__(self):
        r_str = "Payment made: {0}\nBooking: {1}\nAccount: {2}".format(self.date_of_payment, self.booking, self.account)
        return r_str
    
class GuessTransaction(models.Model):
    date_of_payment = models.DateTimeField(null=False)
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT)
    card_details = models.ForeignKey(CardDetails, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        r_str = "{0} {1} {2}".format(self.booking, self.card_details, self.date_of_payment)
        return r_str