from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import Group, User
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict

from .models import *
from .forms import *
from decorators import allowed_users

# @allowed_users(['club reps'])
def newBooking(request):

    return HttpResponse('needs implementing')

    # form = forms.NewShowingsForm(request.POST or None)
    
    # if request.method == "POST":
        
    #     if form.is_valid():

    #         showing = form.save()

    #         return redirect('showing-all')
    #     else:
    #         return render(request, 'showings/showing_new.html', {
    #             "form":form,
    #             "film":request.POST.get('form-0-film-id'),
    #             "time":request.POST.get('form-1-time'),
    #             "date":request.POST.get('form-2-date')
    #             })
        
    # else:
    #     form = forms.NewShowingsForm()
    #     return render(request, 'showings/showing_new.html', {"form":form})