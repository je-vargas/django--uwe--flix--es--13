from django.db import models
from django.urls import reverse
import uuid


class Film(models.Model):
    title = models.CharField(max_length=50, null=False)
    age_rating = models.CharField(max_length=20)
    duration = models.IntegerField(null=False)
    film_description = models.CharField(max_length=500, null=False)
    release_date = models.DateField()
    
    #* get_absolute_url needs to be added to every model along with __str__
    def __str__(self):
        return self.title[:50]

    #* get_absolute_url - redirects after submitting a from to film detail
    def get_absolute_url(self):
        print(self)
        return reverse("film-details", args=[str(self.id)])

class Screen(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    
    def __str__(self):
        r_str = "{0}".format(self.number)
        return r_str

class Showing(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.CharField(max_length=50)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        r_str = "{0} {1} {2} {3}".format(self.film, self.time, self.date, self.screen)
        return r_str



