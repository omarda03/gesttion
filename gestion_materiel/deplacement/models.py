from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class Chantier(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.TextField()

    def __str__(self):
        return self.nom

class Materiel(models.Model):
    chantier = models.ForeignKey(Chantier, related_name='materiels', on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantite = models.IntegerField()
    prix_unit_ht = models.DecimalField(max_digits=10, decimal_places=2)
    prix_unit_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    prix_total_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    date_entree = models.DateField()
    note = models.TextField()

    def __str__(self):
        return self.designation

class Deplacement(models.Model):
    chantier_depart = models.ForeignKey(Chantier, related_name='departs', on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantite = models.IntegerField()
    chantier_destination = models.ForeignKey(Chantier, related_name='destinations', on_delete=models.CASCADE)
    date_deplacement = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.materiel.designation} de {self.chantier_depart.nom} à {self.chantier_destination.nom}'

    def save(self, *args, **kwargs):
        if self.quantite > self.materiel.quantite:
            raise ValueError("Quantité à déplacer dépasse la quantité disponible")
        super().save(*args, **kwargs)
