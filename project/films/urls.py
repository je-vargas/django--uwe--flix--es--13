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
    path("<int:pk>/delete/", FilmDeleteView.as_view(), name="film_delete"),
    path("<int:pk>/update/", FilmUpdateView.as_view(), name="film_update"),
    path("<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("new/", FilmNewView.as_view(), name="film_new")
]