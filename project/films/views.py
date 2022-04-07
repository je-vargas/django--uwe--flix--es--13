from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .models import Film, Showing
from . import forms

class HomePageView(ListView):
    model = Film
    template_name = 'home.html'
    context_object_name = "all_films"

class FilmsDetailView(DetailView):
    model = Film
    template_name = 'films/film_detail.html'

class FilmsNewView(LoginRequiredMixin, CreateView):
    model = Film
    template_name = 'films/film_new.html'
    login_url = 'login', 
    form_class = forms.NewFilmsForm

class FilmsUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    template_name = 'films/film_update.html'
    login_url = 'login'
    form_class = forms.UpdateFilmForm

class FilmsDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    template_name = template_name = 'films/film_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    # def dispatch(self, request, *args, **kwargs): 
        #     obj = self.get_object()
        #     if obj.author != self.request.user:
        #         raise PermissionDenied
        #     return super().dispatch(request, *args, **kwargs)

def showingsNewView(request):

    form = forms.NewShowingsForm(request.POST or None)
    
    if request.method == "POST":
        
        if form.is_valid():
            date = form.cleaned_data['date'],
            time = form.cleaned_data['time'],
            film_id = form.cleaned_data['film_id']

            print(f"time: {time}\ndate: {date}\nfilm: {film_id}")

            showing = form.save(commit=False)
            
            print(f"obj: {showing}")
            showing.save()

            return redirect('showings-all')
        else:
            return render(request, 'showings/showing_new.html', {
                "form":form,
                "film_id":request.POST.get('form-0-film-id'),
                "time":request.POST.get('form-1-time'),
                "date":request.POST.get('form-2-date')
                })
        
    else:
        form = forms.NewShowingsForm()
        return render(request, 'showings/showing_new.html', {"form":form})



class ShowingsAllView(ListView):
    model = Showing
    template_name = 'showings/showing_all.html'
    context_object_name = "all_showings"

class ShowingDetailView(LoginRequiredMixin, DetailView):
    model = Showing
    template_name = 'showings/showing_detail.html'

class ShowingUpdateView(LoginRequiredMixin, UpdateView):
    model = Showing
    template_name = 'showings/showing_update.html'
    success_url = reverse_lazy('showing-all')
    login_url = 'login'
    form_class=forms.UpdateShowingForm

class ShowingDeleteView(LoginRequiredMixin, DeleteView):
    model = Showing
    template_name = template_name = 'showings/showing_delete.html'
    success_url = reverse_lazy('showing-all')
    login_url = 'login'

class AboutPageView(TemplateView):
    template_name = 'about.html'