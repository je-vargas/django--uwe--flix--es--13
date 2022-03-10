from django.urls import path
from .views import HomePageView, AboutPageView, FilmDetailView

urlpatterns = [
    path("films/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home")
]