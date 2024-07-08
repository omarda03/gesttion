from django.contrib import admin
from .models import Chantier, Materiel, Deplacement

# Register your models here.

@admin.register(Chantier)
class ChantierAdmin(admin.ModelAdmin):
    list_display = ['nom']

@admin.register(Materiel)
class MaterielAdmin(admin.ModelAdmin):
    list_display = ['designation', 'description']

@admin.register(Deplacement)
class DeplacementAdmin(admin.ModelAdmin):
    list_display = ['chantier_depart', 'materiel', 'quantite', 'chantier_destination', 'date_deplacement']
    list_filter = ['chantier_depart', 'chantier_destination', 'date_deplacement']
    search_fields = ['materiel__designation', 'description']
