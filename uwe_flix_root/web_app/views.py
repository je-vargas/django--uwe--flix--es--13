from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home response is currently working</h1>")


def club_rep_login(request):
    return HttpResponse("the club rep url works")
