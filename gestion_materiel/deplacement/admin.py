# deplacement/admin.py

from django.contrib import admin
from .models import Materiel, Chantier, Deplacement

class MaterielAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'quantite', 'chantier')

admin.site.register(Materiel, MaterielAdmin)
admin.site.register(Chantier)
admin.site.register(Deplacement)
