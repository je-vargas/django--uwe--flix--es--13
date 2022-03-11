from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Film

template_root = "web_app"

class HomePageView(ListView):
    model = Film
    template_name = f'{template_root}/home.html'
    context_object_name = "all_films"

class FilmDetailView(DetailView):
    model = Film
    template_name = f'{template_root}/film_detail.html'

class FilmNew(CreateView):
    model = Film
    template_name = f'{template_root}/film_new.html'
    fields = '__all__'

class FilmUpdate(UpdateView):
    model = Film
    template_name = template_name = f'{template_root}/film_update.html'
    # fields = [""]
    fields = '__all__'

class AboutPageView(TemplateView):
    template_name = f'{template_root}/about.html'
