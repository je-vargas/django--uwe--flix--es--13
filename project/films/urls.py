from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("films/<int:pk>/delete/", views.FilmsDeleteView.as_view(), name="film-delete"),
    path("films/<int:pk>/update/", views.FilmsUpdateView.as_view(), name="film-update"),
    path("films/<int:pk>/", views.FilmsDetailView.as_view(), name="film-detail"),
    path("films/new/", views.FilmsNewView.as_view(), name="film-new"),

    path("showings/<int:pk>/", views.ShowingDetailView.as_view(), name="showings-details"),
    path("showings/new", views.showingsNewView, name="showings-new"),
    # path("showings/new", views.ShowingsNewView.as_view(), name="showing-new"),
    path("showings/", views.ShowingsAllView.as_view(), name="showings-all"),
    
    # path("showing/<int:pk>/delete/", views.as_view(), name="film-delete"),
    # path("showing/<int:pk>/update/", views.as_view(), name="film-update"),
    # path("showing/<int:pk>/", views.as_view(), name="film-detail"),
    
]