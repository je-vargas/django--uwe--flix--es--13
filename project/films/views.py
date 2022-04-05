from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Film, Showing
from .forms import NewFilmsForm, NewShowingsForm

class HomePageView(ListView):
    model = Film
    template_name = 'home.html'
    context_object_name = "all_films"

class FilmsDetailView(DetailView):
    model = Film
    template_name = 'film_detail.html'

class FilmsNewView(LoginRequiredMixin, CreateView):
    model = Film
    template_name = 'film_new.html'
    login_url = 'login', 
    form_class = NewFilmsForm

class FilmsUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    template_name = 'film_update.html'
    fields = '__all__'
    login_url = 'login'

class FilmsDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    template_name = template_name = 'film_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    # def dispatch(self, request, *args, **kwargs): 
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)



class ShowingsNewView(LoginRequiredMixin, CreateView):
    model = Showing
    form_class = NewShowingsForm
    template_name = 'showing_new.html'
    success_url = reverse_lazy('showing-all')

class ShowingsAllView(ListView):
    model = Showing
    template_name = 'showing_all.html'
    context_object_name = "all_showings"

class ShowingDetailView(LoginRequiredMixin, DetailView):
    model = Showing
    template_name = 'showing_detail.html'

class ShowingUpdateView(LoginRequiredMixin, UpdateView):
    model = Showing
    template_name = 'film_update.html'
    fields = '__all__'
    login_url = 'login'

class ShowingDeleteView(LoginRequiredMixin, DeleteView):
    model = Showing
    template_name = template_name = 'film_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

class AboutPageView(TemplateView):
    template_name = 'about.html'