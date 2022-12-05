from django.urls import path, include
from . import views

app_name = 'tvapp'
urlpatterns = [
    path('', views.index_view, name='tv_library'),
    path('series/<int:nid>', views.detailed_series_view, name='detailed_series_view'),
    path('series/<int:nid>/season/<int:seid>', views.detailed_season_view, name='detailed_season_view'),
    path('series/<int:nid>/season/<int:seid>/episode/<int:eid>', views.detailed_episode_view, name='detailed_episode_view'),
    path('create', views.create_series_view, name='new_series'),
    path('series/<int:nid>/season/create', views.create_season_view, name='new_season'),
    path('series/<int:nid>/season/<int:seid>/episode/create', views.create_episode_view, name='new_episode'),
    path('series/edit/<int:nid>', views.update_series_view, name='series_update'),
    path('series/<int:nid>/season/edit/<int:seid>', views.update_season_view, name='season_update'),
    path('series/<int:nid>/season/<int:seid>/episode/edit/<int:eid>', views.update_episode_view, name='episode_update'),
    path('series/delete/<int:nid>', views.delete_series_view, name='series_delete'),
    path('series/<int:nid>/season/delete/<int:seid>', views.delete_season_view, name='season_delete'),
    path('series/<int:nid>/season/<int:seid>/episode/delete/<int:eid>', views.delete_episode_view, name='episode_delete'),
]