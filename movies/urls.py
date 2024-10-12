from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.index, name="home"),
    path("movies-list/",views.movies, name="movies-list")
]