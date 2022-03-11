from django.urls import path
from .views import HomePageView, AboutPageView, FilmDetailView, FilmNew, FilmUpdate

urlpatterns = [
    path("films/<int:pk>/update", FilmUpdate.as_view(), name="film_update"),
    path("films/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("films/new/", FilmNew.as_view(), name="film_new"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home")
]