from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"

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
            return redirect('login')
    else: 
        return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Sucessfull!"))
            return redirect('home')
    else: 
        form = UserCreationForm()
    return render(request, "registration/signup.html", {
        'form':form,
    })



   