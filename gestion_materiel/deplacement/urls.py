# deplacement/urls.py

from django.urls import path
from .views import accueil, inventaire, materiel, deplacement_view, deplacement_success_view

urlpatterns = [
    path('', accueil, name='accueil'),
    path('inventaire/', inventaire, name='inventaire'),
    path('materiel/', materiel, name='materiel'),
    path('deplacement/', deplacement_view, name='deplacement'),
    path('deplacement/success/', deplacement_success_view, name='deplacement_success'),
]
