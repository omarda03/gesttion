from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('materiel/', views.materiel, name='materiel'),
    path('inventaire/', views.inventaire, name='inventaire'),
    path('deplacement/', views.deplacement, name='deplacement'),
    path('materiaux_par_chantier/<int:chantier_id>/', views.materiaux_par_chantier, name='materiaux_par_chantier'),
]
