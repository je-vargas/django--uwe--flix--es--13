from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .models import Film, Showing, Screen
from . import forms
from decorators import allowed_users


class HomePageView(ListView):
    model = Film
    template_name = 'home.html'
    context_object_name = "all_films"

class FilmsDetailView(DetailView):
    model = Film
    template_name = 'films/film_detail.html'

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class FilmsNewView(LoginRequiredMixin, CreateView):
    model = Film
    template_name = 'films/film_new.html'
    login_url = 'login-user'
    form_class = forms.NewFilmsForm

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class FilmsUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    template_name = 'films/film_update.html'
    login_url = 'login-user'
    form_class = forms.UpdateFilmForm

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class FilmsDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    template_name = 'films/film_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login-user'

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

@allowed_users(['cinema manager', 'staff'])
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
            return render(request, 'screens/_new.html', {
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

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ShowingDetailView(LoginRequiredMixin, DetailView):
    model = Showing
    template_name = 'showings/showing_detail.html'

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ShowingUpdateView(LoginRequiredMixin, UpdateView):
    model = Showing
    template_name = 'showings/showing_detail_update.html'
    success_url = reverse_lazy('screen-all')
    login_url = 'login-user'
    form_class=forms.UpdateShowingForm

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ShowingDeleteView(LoginRequiredMixin, DeleteView):
    model = Showing
    template_name = template_name = 'showings/showing_detail_delete.html'
    success_url = reverse_lazy('screen-all')
    login_url = 'login-user'

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ScreenAllView(ListView):
    model = Screen
    template_name = 'screens/screen_all.html'
    context_object_name = "all_screens"
    success_url = reverse_lazy('screen-all')

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ScreenDetailView(LoginRequiredMixin, DetailView):
    model = Screen
    template_name = 'screens/screen_detail.html'

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    

class ScreenUpdateView(LoginRequiredMixin, UpdateView):
    model = Screen
    template_name = 'screens/screen_update.html'
    login_url = 'login-user'
    form_class = forms.UpdateScreenForm
    success_url = reverse_lazy('screen-all')

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ScreenDeleteView(LoginRequiredMixin, DeleteView):
    model = Screen
    template_name = template_name = 'screens/screen_delete.html'
    login_url = 'login-user'
    success_url = reverse_lazy('screen-all')

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ScreenNewView(LoginRequiredMixin, CreateView):
    model = Screen
    template_name = 'screens/screen_new.html'
    login_url = 'login-user', 
    form_class = forms.NewScreenForm
    success_url = reverse_lazy('screen-all')

    @allowed_users(['cinema manager, staff'])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AboutPageView(TemplateView):
    template_name = 'about.html'