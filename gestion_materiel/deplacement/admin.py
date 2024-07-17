from django.contrib import admin
from .models import Chantier, Materiel, Deplacement

class DeplacementAdmin(admin.ModelAdmin):
    list_display = ('materiel', 'chantier_depart', 'chantier_destination', 'quantite', 'date_deplacement')
    fields = ('materiel', 'chantier_depart', 'chantier_destination', 'quantite', 'description')

admin.site.register(Chantier)
admin.site.register(Materiel)
admin.site.register(Deplacement, DeplacementAdmin)
