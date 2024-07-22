from django.contrib import admin
from .models import Chantier, Materiel, Deplacement

class DeplacementAdmin(admin.ModelAdmin):
    list_display = ('materiel', 'chantier_depart', 'chantier_destination', 'quantite', 'date_deplacement', 'description')
    fields = ('materiel', 'chantier_depart', 'chantier_destination', 'quantite', 'date_deplacement', 'description')

admin.site.register(Chantier)
admin.site.register(Materiel)
admin.site.register(Deplacement, DeplacementAdmin)
