
from django.urls import path
from . import views

urlpatterns = [
    path('', views.films, name='films'),
    path('film/<str:film_name>/', views.film_detail, name='film_details'),
    path('confirmation/', views.confirmation, name='confirmation'),
]