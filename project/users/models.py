from django.db import models
class Club(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254)
    mobile = models.IntegerField()
    landline = models.CharField(max_length=20)
    house_number: models.IntegerField(null=False)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        r_str = "{0}".format(self.name)
        return r_str
    

    