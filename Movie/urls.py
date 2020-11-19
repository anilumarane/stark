from django.urls import path
from . import views
from .cms import poster, cmsmovies

urlpatterns = [
    # path('', views.poster),
    path('poster_create', poster.poster_create),
    path('poster_update/<int:poster_id>', poster.poster_update),
    path('poster_delete/<int:poster_id>', poster.poster_delete),


    path('movie_create', cmsmovies.movie_create),
    path('movie_update/<int:movie_id>', cmsmovies.movie_update),
    path('movie_delete/<int:movie_id>', cmsmovies.movie_delete),


    path('get_movie_list', views.get_movie_list),
    path('get_movies', views.get_movies),

]
