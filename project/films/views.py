from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Film

class HomePageView(ListView):
    model = Film
    template_name = 'home.html'
    context_object_name = "all_films"

class FilmDetailView(DetailView):
    model = Film
    template_name = 'film_detail.html'

class FilmNewView(LoginRequiredMixin, CreateView):
    model = Film
    template_name = 'film_new.html'
    fields = '__all__'
    login_url = 'login'

class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    template_name = template_name = 'film_update.html'
    fields = '__all__'
    login_url = 'login'
class FilmDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    template_name = template_name = 'film_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    # def dispatch(self, request, *args, **kwargs): 
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)

class AboutPageView(TemplateView):
    template_name = 'about.html'
