from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("films/<int:pk>/delete/", views.FilmsDeleteView.as_view(), name="film-delete"),
    path("films/<int:pk>/update/", views.FilmsUpdateView.as_view(), name="film-update"),
    path("films/<int:pk>/", views.FilmsDetailView.as_view(), name="film-details"),
    path("films/new/", views.FilmsNewView.as_view(), name="film-new"),

    path("showings/", views.ShowingsAllView.as_view(), name="showing-all"),
    path("showing/<int:pk>/delete/", views.ShowingDeleteView.as_view(), name="showing-delete"),
    path("showing/<int:pk>/update/", views.ShowingUpdateView.as_view(), name="showing-update"),
    path("showings/<int:pk>/", views.ShowingDetailView.as_view(), name="showing-details"),
    path("showings/new", views.showingsNewView, name="showing-new"),
    
]