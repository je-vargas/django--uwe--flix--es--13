from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Film

template_root = "web_app"

class HomePageView(ListView):
    model = Film
    template_name = f'{template_root}/home.html'
    context_object_name = "all_films"

class FilmDetailView(DetailView):
    model = Film
    template_name = f'{template_root}/film_detail.html'

class AboutPageView(TemplateView):
    template_name = f'{template_root}/about.html'
