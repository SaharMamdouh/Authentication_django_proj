from django.urls import path
from .views import movie , movies , update ,delete , view

app_name='movie'
urlpatterns = [

   path('movie/', movie , name='movie-data'),
   path('movies/', movies , name='movies-data'),
   path('movies/<movie_id>', update , name='update-data'),
   path('movies/delete/<movie_id>', delete , name='delete-data'),
   path('movies/view/<movie_id>', view , name='view-data'),
]