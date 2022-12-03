from django.urls import path, include
from . import views

app_name = 'homeapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('browse/', views.browse, name='browse'),
]
