from django.urls import path, include
from . import views

app_name = 'movieapp'
urlpatterns = [
    path('', views.index_view, name='movie_library'),
    path('create', views.create_view, name='new_movie'),
]
