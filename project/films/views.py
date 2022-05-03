from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group, User
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict

from .models import Film, Showing, Screen
from . import forms
from decorators import allowed_users


class HomePageView(ListView):
    model = Film
    template_name = 'home.html'
    context_object_name = "all_films"

class FilmsDetailView(DetailView):
    model = Film, User
    template_name = 'films/film_detail.html'

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def get(self, *args, **kwargs):
        film = get_object_or_404(Film, pk=self.kwargs.get('pk'))
        return render(self.request, 'films/film_detail.html', {'film':film})

class FilmsNewView(LoginRequiredMixin, CreateView):
    model = Film
    template_name = 'films/film_new.html'
    login_url = 'login-user'
    form_class = forms.NewFilmsForm
    success_url = 'home'

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def post(self, *args, **kwargs):
        request = self.request

        form = forms.NewFilmsForm(request.POST or None)
        if request.method == 'POST':   

            if form.is_valid():
                form.save()
                return redirect('home')
            else: 
                return render(request, 'films/film_new.html', {
                    'form':form,
                    'title':request.POST.get('title'), 
                    'age_rating':request.POST.get('age_rating'),
                    'duration':request.POST.get('duration'),
                    'film_description':request.POST.get('film_description'),
                    'release_date':request.POST.get('release_date')
                })
        
        new_film = forms.NewFilmsForm()
        return render(self.request, 'films/film_new.html', {'form': new_film})

class FilmsUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    template_name = 'films/film_update.html'
    login_url = 'login-user'
    form_class = forms.UpdateFilmForm

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def patch(self, *args, **kwargs):
        film_object = get_object_or_404(Film, pk=self.kwargs.get('pk'))
        film = model_to_dict(film_object)
        form = forms.UpdateFilmForm(film)

        if form.is_valid():
            form.save()
            return redirect('film-details')

        return render(self.request, 'films/film_update.html', {
            'form': form,
            'film': film_object
            })

class FilmsDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    template_name = 'films/film_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login-user'

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def delete(self, *args, **kwargs):
        
        film_object = get_object_or_404(Film, pk=self.kwargs.get('pk'))
        
        if self.request.method == "POST":
            film_object.delete()
            return redirect('home')
        return render(self.request, 'showings/film_delete.html')

@allowed_users(['cinema manager', 'staff'])
def showingsNewView(request):

    form = forms.NewShowingsForm(request.POST or None)
    
    if request.method == "POST":
        
        if form.is_valid():
            date = form.cleaned_data['date'],
            time = form.cleaned_data['time'],
            film = form.cleaned_data['film']

            print(f"time: {time}\ndate: {date}\nfilm: {film}")

            showing = form.save()

            return redirect('showing-all')
        else:
            return render(request, 'showings/showing_new.html', {
                "form":form,
                "film":request.POST.get('form-0-film-id'),
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

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def get(self, *args, **kwargs):
        showings = Showing.objects.all()
        return render(self.request, 'showings/showing_all.html', {
            'all_showings':showings
        })

class ShowingDetailView(LoginRequiredMixin, DetailView):
    model = Showing
    template_name = 'showings/showing_detail.html'

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def get(self, *args, **kwargs):
        showing = get_object_or_404(Showing, pk=self.kwargs.get('pk'))
        return render(self.request, 'showings/showing_detail.html', {'showing':showing})

class ShowingUpdateView(LoginRequiredMixin, UpdateView):
    model = Showing
    template_name = 'showings/showing_update.html'
    success_url = reverse_lazy('screen-all')
    login_url = 'login-user'
    form_class=forms.UpdateShowingForm

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def patch(self, *args, **kwargs):
        showing_object = get_object_or_404(Showing, pk=self.kwargs.get('pk'))
        showing = model_to_dict(showing_object)
        form = forms.UpdateFilmForm(showing)

        if form.is_valid():
            form.save()
            return redirect('showing-details')

        return render(self.request, 'showings/showing_update.html', {
            'form': form,
            'showing':showing_object
            })

class ShowingDeleteView(LoginRequiredMixin, DeleteView):
    model = Showing
    template_name = 'showings/showing_delete.html'
    success_url = reverse_lazy('showing-all')
    login_url = 'login-user'

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def delete(self, *args, **kwargs):

        showing_object = get_object_or_404(Showing, pk=self.kwargs.get('pk'))
        
        if self.request.method == "POST":
            showing_object.delete()
            return redirect('home')
        return render(self.request, 'showings/showing_delete.html')

class ScreenAllView(ListView):
    model = Screen
    template_name = 'screens/screen_all.html'
    context_object_name = "all_screens"
    success_url = reverse_lazy('screen-all')

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def get(self, *args, **kwargs):
        screens = Screen.objects.all()
        return render(self.request, 'screens/screen_all.html', {
            'all_screens' : screens
        })

class ScreenDetailView(LoginRequiredMixin, DetailView):
    model = Screen
    template_name = 'screens/screen_detail.html'

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def get(self, *args, **kwargs):
        screen = get_object_or_404(Screen, pk=self.kwargs.get('pk'))
        return render(self.request, 'screens/screen_detail.html', {'screen':screen})
        
class ScreenUpdateView(LoginRequiredMixin, UpdateView):
    model = Screen
    template_name = 'screens/screen_update.html'
    login_url = 'login-user'
    form_class = forms.UpdateScreenForm
    success_url = reverse_lazy('screen-all')

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def patch(self, *args, **kwargs):
        screen_object = get_object_or_404(Screen, pk=self.kwargs.get('pk'))
        screen = model_to_dict(screen_object)
        form = forms.UpdateFilmForm(screen)

        if form.is_valid():
            form.save()
            return redirect('screen-details')

        return render(self.request, 'screens/screen_update.html', {
            'form': form,
            'screen':screen_object
            })

class ScreenDeleteView(LoginRequiredMixin, DeleteView):
    model = Screen
    template_name = template_name = 'screens/screen_delete.html'
    login_url = 'login-user'
    success_url = reverse_lazy('screen-all')

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def delete(self, *args, **kwargs):

        screen_object = get_object_or_404(Screen, pk=self.kwargs.get('pk'))
        
        if self.request.method == "POST":
            screen_object.delete()
            return redirect('home')
        return render(self.request, 'screens/screen_delete.html')

class ScreenNewView(LoginRequiredMixin, CreateView):
    model = Screen
    template_name = 'screens/screen_new.html'
    login_url = 'login-user', 
    form_class = forms.NewScreenForm
    success_url = reverse_lazy('screen-all')

    @method_decorator(allowed_users(['cinema manager', 'staff']))
    def post(self, *args, **kwargs):
        request = self.request

        if request.method == 'POST':   
            form = forms.NewScreenForm(request.POST or None)

            if form.is_valid():
                form.save()
                return redirect('screen-all')
            else: 
                return render(request, 'screens/screen_new.html', {
                    'form':form,
                    'screen_number':request.POST.get('screen_number'), 
                    'screen_sscreen_seats_number':request.POST.get('screen_sscreen_seats_number'),
                })
        
        new_screen = forms.NewScreenForm()
        return render(self.request, 'screens/screen_new.html', {'form': new_screen})

class AboutPageView(TemplateView):
    template_name = 'about.html'