from django.views.generic.base import TemplateView
from django.views.generic import ListView
from . import models

template_root = "web_app"

class HomePageView(ListView):
    model = models.Film
    template_name = f'{template_root}/home.html'
    context_object_name = "all_films"
class AboutPageView(TemplateView):
    template_name = f'{template_root}/about.html'
