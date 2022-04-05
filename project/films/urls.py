from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    FilmsDetailView,
    FilmsNewView,
    FilmsUpdateView,
    FilmsDeleteView,
    ShowingsNewView,
    ShowingsAllView, 
    ShowingDetailView
) 

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path("films/<int:pk>/delete/", FilmsDeleteView.as_view(), name="film-delete"),
    path("films/<int:pk>/update/", FilmsUpdateView.as_view(), name="film-update"),
    path("films/<int:pk>/", FilmsDetailView.as_view(), name="film-detail"),
    path("films/new/", FilmsNewView.as_view(), name="film-new"),

    path("showings/<int:pk>/", ShowingDetailView.as_view(), name="showing-details"),
    path("showings/new", ShowingsNewView.as_view(), name="showing-new"),
    path("showings/", ShowingsAllView.as_view(), name="showing-all"),
    
    # path("showing/<int:pk>/delete/", .as_view(), name="film-delete"),
    # path("showing/<int:pk>/update/", .as_view(), name="film-update"),
    # path("showing/<int:pk>/", .as_view(), name="film-detail"),
    
]