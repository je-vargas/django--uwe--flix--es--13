from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from decorators import unauthenticated_user, allowed_users
from access import * 
from .forms import RegisterUserForm
from .models import *

@unauthenticated_user 
def login_user(request):    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an error login in, try again")
            return redirect('login-user')
    else: 
        return render(request, 'registration/login.html', {})

def logout_user(request):    
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    user_groups = None
    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user_form = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            group = Group.objects.get(name='student')
            user_form.groups.add(group)

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Sucessfull!"))
            return redirect('home')

    else: 
        form = RegisterUserForm()
        user_groups = get_user_groups(request)

    return render(request, "registration/register.html", {
        'form':form,
        'user_groups': user_groups
    })

@allowed_users(['cinema manager'])
def register_clubrep_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)


        if form.is_valid():
            user_form = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            group = Group.objects.get(name='club rep')
            user_form.groups.add(group)

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Sucessfull!"))
            return redirect('home')
    
    form = RegisterUserForm()
    user_groups = get_user_groups(request)
    return render(request, "registration/register.html", {
        'form':form,
        'user_groups': user_groups
    })

@allowed_users(['admin'])
def register_backoffice_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user_form = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            role = form.cleaned_data['role']

            print(type(role))

            group = Group.objects.get(name=role)
            user_form.groups.add(group)

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Sucessfull!"))
            return redirect('home')
    else: 
        form = RegisterUserForm()
        user_groups = get_user_groups(request)
        return render(request, "registration/register.html", {
            'form':form,
            'user_groups': user_groups
        })



   