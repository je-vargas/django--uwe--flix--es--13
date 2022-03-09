from django.views.generic.base import TemplateView

template_root = "web_app"

class HomePageView(TemplateView):
    template_name = f'{template_root}/home.html'
class AboutPageView(TemplateView):
    template_name = f'{template_root}/about.html'
