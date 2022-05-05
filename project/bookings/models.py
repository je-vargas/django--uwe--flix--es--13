from django.db import models

class TicketType(models.Model):
    ticket = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.ticket

class CardDetails(models.Model):
    card_number = models.BigIntegerField(null=False)
    expiry_date = models.DateField(null=False)

    def __str__(self):
        r_str = "{0} {1}".format(self.card_number, self.expiry_date)
        return r_str


class Account(models.Model):
    account_title = models.CharField(max_length=50, null=False)
    account_discount = models.BigIntegerField(null=True)
    card_details = models.ForeignKey(CardDetails, on_delete=models.PROTECT)

    def __str__(self):
        return self.account_title + " " + self.account_discount

class Booking(models.Model):
    ticket = models.ForeignKey(TicketType, on_delete=models.PROTECT)
    booking_cost = models.IntegerField(null=False)
    number_of_tickets = models.IntegerField(null=False)
    showing = models.ForeignKey('films.Showing', on_delete=models.PROTECT)
    
    def __str__(self):
        r_str = "{0} {1} {2} {3}".format(self.booking_cost, self.number_of_tickets, self.ticket, self.showing)
        return r_str

class LoginTransaction(models.Model):
    date_of_payment = models.DateTimeField(null=False)
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    club = models.ForeignKey('users.Club', on_delete=models.PROTECT)
    
class GuessTransaction(models.Model):
    date_of_payment = models.DateTimeField(null=False)
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT)
    card_details = models.ForeignKey(CardDetails, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        r_str = "{0} {1} {2}".format(self.booking, self.card_details, self.date_of_payment)
        return r_str