from django.urls import path
from .views import accueil,inventaire,materiel,deplacement

urlpatterns = [
    path('deplacement/', deplacement, name='deplacement'),
    path('', accueil, name='accueil'),
    path('inventaire/', inventaire, name='inventaire'),
    path('materiel/', materiel, name='materiel'),
   
]
