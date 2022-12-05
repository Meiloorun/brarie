from django.urls import path, include
from . import views

app_name = 'peopleapp'
urlpatterns = [
    path('', views.index_view, name='people_index'),
    path('create', views.create_view, name='new_person'),
    path('<int:nid>', views.detail_view, name='person_detail'),
    path('edit/<int:nid>', views.update_view, name='person_update'),
    path('delete/<int:nid>', views.delete_view, name='person_delete'),
]