from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    FilmDetailView,
    FilmNewView,
    FilmUpdateView,
    FilmDeleteView
) 

urlpatterns = [
    path("films/<int:pk>/delete/", FilmDeleteView.as_view(), name="film_delete"),
    path("films/<int:pk>/update/", FilmUpdateView.as_view(), name="film_update"),
    path("films/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("films/new/", FilmNewView.as_view(), name="film_new"),
    path("", HomePageView.as_view(), name="home")
]