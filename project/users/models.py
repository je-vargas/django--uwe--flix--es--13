from django.db import models
class Club(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=13)
    landline = models.CharField(max_length=13)
    house_number = models.CharField(max_length=3000)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    discount = models.FloatField(null=True)
    account_number = models.UUIDField(null=True)

    def __str__(self):
        r_str = "{0}".format(self.name)
        return r_str
    

    