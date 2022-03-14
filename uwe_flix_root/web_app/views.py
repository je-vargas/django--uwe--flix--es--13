from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Film

class HomePageView(ListView):
    model = Film
    template_name = 'home.html'
    context_object_name = "all_films"

class FilmDetailView(DetailView):
    model = Film
    template_name = 'film_detail.html'

class FilmNewView(CreateView):
    model = Film
    template_name = 'film_new.html'
    fields = '__all__'

class FilmUpdateView(UpdateView):
    model = Film
    template_name = template_name = 'film_update.html'
    fields = '__all__'
class FilmDeleteView(DeleteView):
    model = Film
    template_name = template_name = 'film_delete.html'
    success_url = reverse_lazy('home')

class AboutPageView(TemplateView):
    template_name = 'about.html'
