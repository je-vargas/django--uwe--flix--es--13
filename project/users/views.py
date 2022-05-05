from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from decorators import unauthenticated_user, allowed_users
from access import * 
from .forms import *
from .models import *

#* ------------------ AUTHENTICATION ---------------------
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
    form_errors = None

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
            error = list(form.errors.keys())
            form_errors = form.errors.get(error[0])

    else: 
        form = RegisterUserForm()
        user_groups = get_user_groups(request)
        

    return render(request, "registration/register.html", {
        'form':form,
        'user_groups': user_groups,
        'form_errors' : form_errors
    })

@allowed_users(['cinema manager'])
def register_clubrep_user(request):
    form_errors = None
    user_groups = None
    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            # need to add unique value to club reps only
            user_form = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            group = Group.objects.get(name='club rep')
            user_form.groups.add(group)

            user = authenticate(request, username=username, password=password)
            messages.success(request, ("Registration Sucessfull!"))
            return redirect('clubrep-accounts')
        else:
            error = list(form.errors.keys())
            form_errors = form.errors.get(error[0])
    else:
        form = RegisterUserForm()
        user_groups = get_user_groups(request)

    return render(request, "registration/register.html", {
        'form':form,
        'user_groups': user_groups,
        'form_errors': form_errors
    })

@allowed_users(['admin'])
def register_backoffice_user(request):
    form_errors = None
    user_groups = None

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
            error = list(form.errors.keys())
            form_errors = form.errors.get(error[0])
    else: 
        form = RegisterUserForm()
        user_groups = get_user_groups(request)

    return render(request, "registration/register.html", {
        'form':form,
        'user_groups': user_groups,
        'form_errors': form_errors
    })


#* ------------------ ACCOUNTS ---------------------

@allowed_users(['cinema manager'])
def get_clubRep_accounts(request):
    account = User.objects.filter(groups__name='club rep')
    
    return render(request, "users/accounts.html" , {
        'account': account,
        'update':'clubrep-update',
        'delete':'clubrep-delete',
    })

@allowed_users(['cinema manager'])
def update_clubRep_accounts(request, pk):

    account_obj = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST or None, instance = account_obj)
        if form.has_changed():
            if form.is_valid():
                form.save()
                messages.success(request, 'Club Rep account sucessfully updated')
                return redirect('clubrep-accounts')

        else: messages.warning(request, 'No changes were detected')

    else: form = AccountUpdateForm(instance = account_obj)
    
    return render(request, 'users/account_update.html', {
        "form":form,
        })
    
@allowed_users(['cinema manager'])
def delete_clubRep_accounts(request, pk):

    account_obj = get_object_or_404(User, pk=pk)

    if request.method == 'POST':

        account_obj.delete()
        messages.success(request, 'Account sucessfully deleted')
        return redirect('clubrep-accounts')
    
    return render(request, 'users/account_delete.html', {
        "account":account_obj
    })

@allowed_users(['cinema manager'])
def get_student_accounts(request):
    account = User.objects.filter(groups__name='student')
    
    return render(request, "users/accounts.html" , {
        'account': account,
        'update':'student-update',
        'delete':'student-delete',
    })

@allowed_users(['cinema manager', 'staff'])
def update_student_accounts(request, pk):
    
    account_obj = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST or None, instance = account_obj)
        if form.has_changed():
            if form.is_valid():
                form.save()
                messages.success(request, 'Student account sucessfully updated')
                return redirect('student-accounts')
        else: messages.warning(request, 'No changes were detected')   
            
    else: form = AccountUpdateForm(instance = account_obj)
    
    return render(request, 'users/account_update.html', {
        "form":form,
        })

@allowed_users(['cinema manager', 'staff'])
def delete_student_accounts(request, pk):
    account_obj = get_object_or_404(User, pk=pk)

    if request.method == 'POST':

        account_obj.delete()
        messages.success(request, 'Account sucessfully deleted')
        return redirect('student-accounts')
    
    return render(request, 'users/account_delete.html', {
        "account":account_obj
    })


@allowed_users(['cinema manager', 'staff'])
def register_club(request):
    error=None
    form_errors=None

    if request.method == "POST":
        form = RegisterClubForm(request.POST)

        if form.is_valid():
            club_form = form.save()
            messages.success(request, "Club Registration Sucessfull!")
            return redirect('clubs')
        else:
            error = list(form.errors.keys())
            form_errors = form.errors.get(error[0])
    else: 
        form = RegisterClubForm()

    return render(request, "users/register_club.html", {
        'form':form,
        'form_errors': form_errors
    })

@allowed_users(['cinema manager', 'staff'])
def get_clubs(request):

    clubs = Club.objects.all()
    
    return render(request, "users/clubs.html" , {
        'clubs': clubs,
        'update':'club-update',
        'delete':'club-delete',
    })


@allowed_users(['cinema manager', 'staff'])
def update_club(request, pk):
    club_obj = get_object_or_404(Club, pk=pk)
    
    if request.method == 'POST':
        form = RegisterClubForm(request.POST or None, instance = club_obj)
        if form.has_changed():
            if form.is_valid():
                form.save()
                messages.success(request, 'Club sucessfully updated')
                return redirect('clubs')
        else: messages.warning(request, 'No changes were detected')
        
    else: form = RegisterClubForm(instance = club_obj)
    
    return render(request, 'users/club_update.html', {"form":form})
    

@allowed_users(['cinema manager', 'staff'])
def delete_club(request, pk):
    club_obj = get_object_or_404(Club, pk=pk)

    if request.method == 'POST':
        club_obj.delete()
        messages.success(request, 'Club sucessfully deleted')
        return redirect('clubs')
    
    return render(request, 'users/club_delete.html', {
        "club":club_obj
    })
