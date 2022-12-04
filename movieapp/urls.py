from django.urls import path, include
from . import views

app_name = 'movieapp'
urlpatterns = [
    path('', views.index_view, name='movie_library'),
    path('create', views.create_view, name='new_movie'),
    path('<int:nid>', views.detail_view, name='movie_detail'),
    path('edit/<int:nid>', views.update_view, name='movie_update'),
    path('delete/<int:nid>', views.delete_view, name='movie_delete'),
]
