from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('deplacement/', views.deplacement, name='deplacement'),
    path('inventaire/', views.inventaire, name='inventaire'),
    path('materiel/', views.materiel, name='materiel'),
    path('entree/', views.entree, name='entree'),
    path('materiaux_par_chantier/<int:chantier_id>/', views.materiaux_par_chantier, name='materiaux_par_chantier'),
]
