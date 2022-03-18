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
    path("films/<int:pk>/delete/", FilmDeleteView.as_view(), name="film-delete"),
    path("films/<int:pk>/update/", FilmUpdateView.as_view(), name="film-update"),
    path("films/<int:pk>/", FilmDetailView.as_view(), name="film-detail"),
    path("films/new/", FilmNewView.as_view(), name="film-new"),
    path("", HomePageView.as_view(), name="home")
]