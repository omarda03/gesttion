# deplacement/models.py

from django.db import models

class Chantier(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255, null=True, blank=True)
    quantite = models.IntegerField(default=0)

class Materiel(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE, null=True, default=None)  # Allow null values or provide a default Chantier instance
    quantite = models.IntegerField(default=0)

class Deplacement(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    chantier_depart = models.ForeignKey(Chantier, related_name='depart', on_delete=models.CASCADE)
    chantier_destination = models.ForeignKey(Chantier, related_name='destination', on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_deplacement = models.DateTimeField(auto_now_add=True)
